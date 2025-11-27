const express = require('express');
const bodyParser = require('body-parser');
const initCycleTLS = require('cycletls');

const app = express();
const PORT = 3000;

app.use(bodyParser.json({ limit: '50mb' }));
app.use(bodyParser.urlencoded({ limit: '50mb', extended: true }));

let cycleTLSClient;

(async () => {
    cycleTLSClient = await initCycleTLS();
    console.log('CycleTLS Client Initialized');
})();

app.post('/forward', async (req, res) => {
    if (!cycleTLSClient) {
        return res.status(500).json({ error: 'CycleTLS not ready' });
    }

    try {
        const { method, url, headers, body, cookies, proxy, ja3, userAgent } = req.body;

        const options = {
            headers: headers || {},
            body: body || undefined,
            cookies: cookies || undefined,
            proxy: proxy || undefined,
            userAgent: userAgent || undefined,
            ja3: ja3 || undefined,
            disableRedirect: true
        };

        console.log(`[Forwarding] ${method} -> ${url}-> ${headers}`);

        const response = await cycleTLSClient(url, options, method.toLowerCase());

        // 调试日志：查看返回的数据类型
        // console.log('Response Status:', response.status);
        // console.log('Response Body Type:', typeof response.body);
        console.log(`[Forwarding] ${response} -> ${response.body}`);
        res.json({
            status: response.status,
            headers: response.headers,
            body: response.body, // 如果是 JSON 对象或字符串，express 会自动处理
            cookies: response.cookies
        });

    } catch (error) {
        console.error('Request Error:', error);
        res.status(500).json({ error: error.message });
    }
});

process.on('exit', () => {
    if (cycleTLSClient) cycleTLSClient.exit();
});

app.listen(PORT, () => {
    console.log(`Node.js Forwarder running on http://localhost:${PORT}`);
});