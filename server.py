import asyncio
import json
import uuid
from aiohttp import web

# Store connected browsers
browsers = set()
# Store pending requests: {request_id: future}
pending_requests = {}


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    print("Browser connected!")
    browsers.add(ws)

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                data = json.loads(msg.data)
                # Check if this is a response to a pending request
                req_id = data.get('id')
                if req_id and req_id in pending_requests:
                    future = pending_requests.pop(req_id)
                    if not future.done():
                        future.set_result(data)
            elif msg.type == web.WSMsgType.ERROR:
                print('ws connection closed with exception %s', ws.exception())
    finally:
        browsers.remove(ws)
        print("Browser disconnected")

    return ws


async def rpc_handler(request):
    if not browsers:
        return web.json_response({'error': 'No browser connected'}, status=503)

    try:
        # 1. Parse request from Python Client
        params = await request.json()
        req_id = str(uuid.uuid4())

        # 2. Construct payload for Browser
        payload = {
            'id': req_id,
            'action': 'fetch',
            'url': params.get('url'),
            'method': params.get('method', 'GET'),
            'headers': params.get('headers', {}),
            'body': params.get('body'),
            'cookies': params.get('cookies', {}),  # Pass cookies to browser
        }

        # 3. Create a Future to wait for response
        loop = asyncio.get_running_loop()
        future = loop.create_future()
        pending_requests[req_id] = future

        # 4. Send to a random browser (or the first one)
        # In a real app, you might want to load balance or select specific browser
        ws = next(iter(browsers))
        await ws.send_str(json.dumps(payload))

        # 5. Wait for response (with timeout)
        try:
            result = await asyncio.wait_for(future, timeout=30)
            return web.json_response(result)
        except asyncio.TimeoutError:
            pending_requests.pop(req_id, None)
            return web.json_response({'error': 'Browser timed out'}, status=504)

    except Exception as e:
        return web.json_response({'error': str(e)}, status=500)


app = web.Application()
app.add_routes([
    web.get('/ws', websocket_handler),
    web.post('/rpc', rpc_handler)
])

if __name__ == '__main__':
    print("Starting RPC Server on http://localhost:8080")
    print("1. Inject browser_inject.js into your browser console")
    print("2. Run client.py to send requests")
    web.run_app(app, port=8080)
