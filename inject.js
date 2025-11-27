// Copy this code into your Browser Console (F12) or Tampermonkey Script
(function() {
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
            function clearAllCookies() {
                const domain = '.shenzhenair.com';
                const cookies = document.cookie.split(';');

                for (let cookie of cookies) {
                    const eqPos = cookie.indexOf('=');
                    const name = eqPos > -1 ? cookie.substr(0, eqPos).trim() : cookie.trim();

                    // 清除cookie：设置过期时间为过去
                    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;domain=${domain}`;
                    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
                }
                console.log('🗑️  Cleared all existing cookies');
            }
            if (msg.action === 'fetch') {
                try {
                    // 1. Set Cookies (if provided)
                    clearAllCookies()
                    if (msg.cookies && Object.keys(msg.cookies).length > 0) {
                        for (const [key, value] of Object.entries(msg.cookies)) {
                            // Note: This only works for non-HttpOnly cookies and current domain
                            document.cookie = `${key}=${value};path=/;max-age=86400;domain=.shenzhenair.com`;
                        }
                    }
                    await new Promise(resolve => setTimeout(resolve, 50));

                    // 2. Execute Fetch
                    const response = await fetch(msg.url, {
                        method: msg.method,
                        headers: msg.headers,
                        body: msg.body || undefined,
                        mode: 'cors',
                        credentials: 'include' // Important: Send browser cookies
                    });

                    // 3. Read Body
                    const text = await response.text();

                    // 4. Read Headers
                    const headers = {};
                    response.headers.forEach((value, key) => {
                        headers[key] = value;
                    });

                    // 5. Read Cookies (Current Snapshot)
                    // Note: fetch() hides Set-Cookie header, so we read document.cookie
                    // This returns "key=value; key2=value2" string
                    const currentCookies = {};
                    if (document.cookie) {
                        console.log(document.cookie)
                        document.cookie.split(';').forEach(cookie => {
                            const parts = cookie.split('=');
                            const name = parts[0].trim();
                            const value = parts.slice(1).join('=').trim();
                            if (name) currentCookies[name] = value;
                        });
                    }
                    console.log(currentCookies)

                    // Send back result
                    ws.send(JSON.stringify({
                        id: msg.id,
                        status: response.status,
                        statusText: response.statusText,
                        headers: headers,
                        body: text,
                        cookies: currentCookies // Send back visible cookies
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

    connect();
})();
