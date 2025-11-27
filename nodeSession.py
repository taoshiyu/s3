import requests
import json
from requests.models import Response
from requests.structures import CaseInsensitiveDict

# Node.js 服务的地址
NODE_SERVER_URL = "http://localhost:3000/forward"


class NodeSession(requests.Session):
    def __init__(self, ja3=None, user_agent=None):
        super().__init__()
        self.ja3 = ja3
        self.user_agent = user_agent

    def request(self, method, url, *args, **kwargs):
        # ... (前面的代码保持不变) ...

        # 1. 准备 Headers
        merged_headers = self.headers.copy()
        if 'headers' in kwargs:
            merged_headers.update(kwargs['headers'])

        # [关键修改] 彻底清洗 Accept-Encoding，防止 zstd
        # 找出所有可能的 Accept-Encoding 写法 (如 accept-encoding, ACCEPT-ENCODING)
        keys_to_remove = [k for k in merged_headers.keys() if k.lower() == 'accept-encoding']
        for k in keys_to_remove:
            del merged_headers[k]

        # 强制指定不支持 zstd
        merged_headers['Accept-Encoding'] = 'gzip, deflate, br'

        # 处理 Cookies
        cookies_dict = self.cookies.get_dict()
        if 'cookies' in kwargs:
            cookies_dict.update(kwargs['cookies'])

        # 处理 Body
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

        # 处理代理
        proxy_url = None
        proxies = kwargs.get('proxies', self.proxies)
        if proxies:
            proxy_url = proxies.get('https') or proxies.get('http')
        print(merged_headers)
        # 2. 构建 Payload
        forward_payload = {
            "method": method,
            "url": url,
            "headers": dict(merged_headers),
            "body": payload_body,
            "cookies": cookies_dict,
            "proxy": proxy_url,
            "ja3": self.ja3,
            "userAgent": self.user_agent or merged_headers.get('User-Agent')
        }

        # 3. 发送请求到 Node.js
        try:
            resp = requests.post(NODE_SERVER_URL, json=forward_payload)
            resp_data = resp.json()
        except Exception as e:
            raise requests.exceptions.RequestException(f"Node.js 通信失败: {e}")

        if 'error' in resp_data:
            raise requests.exceptions.RequestException(f"Node.js 报错: {resp_data['error']}")

        # 4. 还原 Response 对象
        response = Response()
        response.status_code = resp_data.get('status', 200)

        # [关键修复] 处理 Headers：将 ["value"] 转换为 "value"
        raw_headers = resp_data.get('headers', {})
        processed_headers = {}
        for k, v in raw_headers.items():
            if isinstance(v, list):
                processed_headers[k] = ', '.join(v)  # 多个值用逗号连接
            else:
                processed_headers[k] = v

        response.headers = CaseInsensitiveDict(processed_headers)

        # 处理 Body
        body_content = resp_data.get('body')
        print(resp_data)
        if body_content is None:
            response._content = b""  # 空响应
        elif isinstance(body_content, str):
            response._content = body_content.encode('utf-8')
        elif isinstance(body_content, dict) or isinstance(body_content, list):
            # 有时候 cycletls 会自动把 json body 转成对象返回，这里将其转回 bytes
            response._content = json.dumps(body_content).encode('utf-8')

        # 处理 Cookies
        if 'cookies' in resp_data and resp_data['cookies']:
            for k, v in resp_data['cookies'].items():
                response.cookies.set(k, v)
                self.cookies.set(k, v)

        response.url = url
        response.request = requests.PreparedRequest()
        response.request.method = method.upper()
        response.request.url = url
        response.request.headers = merged_headers

        return response


# 模块级方法封装
def Session(ja3=None, user_agent=None):
    return NodeSession(ja3=ja3, user_agent=user_agent)


def get(url, **kwargs):
    with NodeSession() as session:
        return session.get(url, **kwargs)


def post(url, **kwargs):
    with NodeSession() as session:
        return session.post(url, **kwargs)