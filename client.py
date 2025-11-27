import requests
import json
from requests.models import Response
from requests.structures import CaseInsensitiveDict

RPC_SERVER_URL = "http://localhost:8080/rpc"


class BrowserRpcSession(requests.Session):
    def request(self, method, url, *args, **kwargs):
        # 1. Prepare headers and body
        merged_headers = self.headers.copy()
        if 'headers' in kwargs:
            merged_headers.update(kwargs['headers'])

        # Handle Body
        payload_body = None
        if 'json' in kwargs:
            payload_body = json.dumps(kwargs['json'])
            merged_headers['Content-Type'] = 'application/json'
        elif 'data' in kwargs:
            if isinstance(kwargs['data'], dict):
                from urllib.parse import urlencode
                payload_body = urlencode(kwargs['data'])
                merged_headers['Content-Type'] = 'application/x-www-form-urlencoded'
            else:
                payload_body = kwargs['data']

        # Handle Cookies
        cookies_dict = self.cookies.get_dict()
        if 'cookies' in kwargs:
            cookies_dict.update(kwargs['cookies'])

        # 2. Send to RPC Server
        rpc_payload = {
            "url": url,
            "method": method,
            "headers": dict(merged_headers),
            "body": payload_body,
            "cookies": cookies_dict
        }

        try:
            resp = requests.post(RPC_SERVER_URL, json=rpc_payload)
            resp.raise_for_status()
            rpc_data = resp.json()
        except Exception as e:
            raise requests.exceptions.RequestException(f"RPC Server Error: {e}")

        if 'error' in rpc_data:
            raise requests.exceptions.RequestException(f"Browser Error: {rpc_data['error']}")

        # 3. Reconstruct Response
        response = Response()
        response.status_code = rpc_data.get('status', 200)
        response.headers = CaseInsensitiveDict(rpc_data.get('headers', {}))

        body_content = rpc_data.get('body', "")
        if isinstance(body_content, str):
            response._content = body_content.encode('utf-8')

        # Handle Cookies from Browser
        if 'cookies' in rpc_data and rpc_data['cookies']:
            for k, v in rpc_data['cookies'].items():
                response.cookies.set(k, v)
                self.cookies.set(k, v)  # Update session cookies

        response.url = url
        response.request = requests.PreparedRequest()
        response.request.method = method.upper()
        response.request.url = url

        return response


# Usage
if __name__ == "__main__":
    session = BrowserRpcSession()

    print("Sending request via Browser RPC...")
    try:
        # Make sure you have run server.py and injected inject.js into a browser!
        r = session.get("https://httpbin.org/get")
        print(f"Status: {r.status_code}")
        print(f"Body: {r.text}")
    except Exception as e:
        print(f"Error: {e}")
        print("Ensure server.py is running and browser is connected!")
