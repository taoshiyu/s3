const WS_URL = 'ws://localhost:8080/ws';
let ws;
let reconnectInterval = 1000;

function connect() {
    ws = new WebSocket(WS_URL);

    ws.onopen = () => {
        console.log('✅ Connected to RPC Server');
        reconnectInterval = 1000;
    };

    ws.onmessage = async (event) => {
        const msg = JSON.parse(event.data);
        console.log('📩 Received Task:', msg);

        if (msg.action === 'fetch') {
            try {
                // 1. Set Proxy (if provided)
                if (msg.proxy) {
                    await setProxy(msg.proxy);
                } else {
                    await clearProxy();
                }

                // 2. Set Cookies (if provided)
                // Note: In Extension, we can use chrome.cookies API for better control
                // But for simplicity and fetch compatibility, we rely on browser's cookie jar
                // If msg.cookies is provided, we might want to set them via chrome.cookies API
                if (msg.cookies && Object.keys(msg.cookies).length > 0) {
                    await setCookies(msg.url, msg.cookies);
                }

                // 3. Execute Fetch
                const response = await fetch(msg.url, {
                    method: msg.method,
                    headers: msg.headers,
                    body: msg.body || undefined,
                    credentials: 'include'
                });

                // 4. Read Body
                const text = await response.text();

                // 5. Read Headers
                const headers = {};
                response.headers.forEach((value, key) => {
                    headers[key] = value;
                });

                // 6. Read Cookies (via chrome.cookies API)
                const cookies = await getCookies(msg.url);

                // Send back result
                ws.send(JSON.stringify({
                    id: msg.id,
                    status: response.status,
                    statusText: response.statusText,
                    headers: headers,
                    body: text,
                    cookies: cookies
                }));
                console.log('📤 Sent Response for', msg.id);

            } catch (error) {
                console.error('❌ Fetch Error:', error);
                ws.send(JSON.stringify({
                    id: msg.id,
                    error: error.message,
                    status: 0
                }));
            }
        }
    };

    ws.onclose = () => {
        console.log('❌ Disconnected. Reconnecting in', reconnectInterval, 'ms...');
        setTimeout(connect, reconnectInterval);
        reconnectInterval = Math.min(reconnectInterval * 2, 30000);
    };

    ws.onerror = (err) => {
        console.error('WebSocket Error:', err);
        ws.close();
    };
}

// --- Helper Functions ---

async function setProxy(proxyUrl) {
    // Parse proxyUrl (e.g., http://user:pass@host:port)
    // chrome.proxy.settings.set requires specific config structure
    // Simple implementation for http/https/socks5

    let scheme = 'http';
    let host = '';
    let port = 80;
    let auth = null;

    try {
        const url = new URL(proxyUrl);
        scheme = url.protocol.replace(':', '');
        host = url.hostname;
        port = parseInt(url.port) || (scheme === 'http' ? 80 : 443);
        if (url.username) {
            // Chrome proxy API doesn't support auth directly in rules for some versions
            // But for simple cases, we might need an extension that handles onAuthRequired
            // For now, let's assume IP auth or handle basic auth if possible
            console.warn('Proxy Auth in URL might not work directly without onAuthRequired listener');
        }
    } catch (e) {
        console.error('Invalid Proxy URL', e);
        return;
    }

    const config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: scheme,
                host: host,
                port: port
            },
            bypassList: ["localhost"]
        }
    };

    return new Promise((resolve) => {
        chrome.proxy.settings.set({ value: config, scope: 'regular' }, () => {
            console.log('Proxy set to', proxyUrl);
            resolve();
        });
    });
}

async function clearProxy() {
    return new Promise((resolve) => {
        chrome.proxy.settings.clear({ scope: 'regular' }, () => {
            console.log('Proxy cleared');
            resolve();
        });
    });
}

async function setCookies(url, cookies) {
    // cookies can be an object {name: value} OR an array of objects [{name, value, domain...}]

    let cookieList = [];
    if (Array.isArray(cookies)) {
        cookieList = cookies;
    } else {
        cookieList = Object.entries(cookies).map(([name, value]) => ({ name, value }));
    }

    const promises = cookieList.map(async (cookie) => {
        const name = cookie.name;
        const value = cookie.value;

        // 1. Try to find existing cookie to preserve metadata if not provided
        let existingCookie = null;
        try {
            existingCookie = await chrome.cookies.get({ url: url, name: name });
        } catch (e) {}

        // 2. Prepare new cookie details
        const newCookieDetails = {
            url: url,
            name: name,
            value: value,
            path: cookie.path || '/',
            secure: cookie.secure,
            httpOnly: cookie.httpOnly
        };

        // 3. Handle Domain
        if (cookie.domain) {
            // User explicitly provided domain (e.g. .shenzhenair.com)
            newCookieDetails.domain = cookie.domain;
        } else if (existingCookie) {
            // Inherit from existing
            newCookieDetails.domain = existingCookie.domain;
            newCookieDetails.path = existingCookie.path;
            newCookieDetails.storeId = existingCookie.storeId;
            newCookieDetails.secure = existingCookie.secure;
            newCookieDetails.httpOnly = existingCookie.httpOnly;
            newCookieDetails.sameSite = existingCookie.sameSite;
        }

        // 4. Remove existing cookie if we are changing domain scope?
        // chrome.cookies.set will overwrite if domain matches.
        // If we are setting domain=.site.com and existing is www.site.com, we might end up with two.
        // To be safe, if we are setting a specific domain, we should probably remove the host-only one if it exists?
        // Or just let chrome handle it. Usually explicit domain is preferred.

        return chrome.cookies.set(newCookieDetails);
    });

    await Promise.all(promises);
}

async function getCookies(url) {
    const cookies = await chrome.cookies.getAll({ url: url });
    const cookieObj = {};
    cookies.forEach(c => {
        cookieObj[c.name] = c.value;
    });
    return cookieObj;
}

// Start connection
connect();
