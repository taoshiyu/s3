import json

import requests

import time
import execjs
from curl_cffi.requests.session import Session
from pprint import pprint
from pyhttpx import HttpSession
from tls_client import Session
from loguru import logger

PROTOCOL_TLSv1_2 = b'\x03\x03'
PROTOCOL_TLSv1_3 = b'\x03\x04'
from nodeSession import NodeSession
from pyhttpx.layers.tls.pyssl import SSLContext

EXT_PAYLOAD = {
    65037: b'\x00\x00\x01\x00\x01\xD2\x00\x20\x8C\xBF\x67\x09\x83\x5B\x11\xAB\x2E\xF7\x9E\x7E\xB4\x0A\xBA\x07\xFE\xE3'
           b'\x7F\xA9\x0D\x4A\x24\x64\x3F\x7E\xFB\x83\x5E\x2B\x98\x75\x00\xB0\x50\x33\x1E\x8B\xB6\x25\x41\x96\x41\xF2'
           b'\x61\x72\xED\xE4\x6F\x0D\x73\x5E\xBE\x87\x9F\x78\x94\x3D\x50\x97\xD0\xFA\x7A\xF7\xD7\x5C\x8D\x86\x07\x96'
           b'\x88\xEB\x95\x56\xB4\x6F\x50\xDE\xD7\x69\xF1\x4A\xED\xD6\x1F\xA0\x96\x83\x5A\xDD\xA5\x91\xCC\xAB\x56\x0E'
           b'\x7C\x33\xFA\xC3\xE8\xDA\x19\x9B\xC0\x11\x55\xC3\x99\x61\xD6\x9C\x38\xC5\xA8\xF6\xEC\xD7\x30\x41\x2E\x84'
           b'\x49\xA1\xBB\xF7\x5F\xE6\x58\x6A\x6E\xA8\x9C\x50\x01\xE8\xA1\xE7\x8F\x0D\x37\xD6\x76\x88\x5C\x0D\x48\xE8'
           b'\x3A\x26\x35\x19\x9C\xDD\x55\x34\x90\x93\x6A\xB5\x8E\x4A\xCE\x42\xCD\x58\xD9\x4E\x1C\x92\xFB\x75\xF6\x3C'
           b'\x3E\x63\x97\x8A\xA5\x74\x90\x44\x81\x01\xF2\x33\xEE\x36\x33\x6A\xE2\x0C\xE7\x0B\xDC\xE9\x63\xDB\x28\x88'
           b'\xA9\x36\x33\x7B\x25\x77\x53\xE4\xA2\x6A'
    }




from client import BrowserRpcSession
import warnings
warnings.filterwarnings('ignore')
def test():
    fcp = 'c2331586'
    cvp = 'c8823e45'
    proxy = requests.get('http://api.tianqiip.com/getip?secret=u4kncdfw&num=1&type=txt&port=1&mr=1&sign=91ac51fd3232c447486480bcb89d831f').text.strip()
    ip_port = proxy.split(':')
    ip = ip_port[0]
    print(ip)
    # ip = None
    proxies = None
    context = execjs.compile(open('get_x_s3_s4e.js', 'r', encoding='utf-8').read())
    # s = HttpSession(
    #     ja3="771,4865-4867-4866-49195-49199-52393-52392-49196-49200-49162-49161-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-34-18-51-43-13-45-28-27-65037,4588-29-23-24-25-256-257,0",
    #     exts_payload=EXT_PAYLOAD,
    # )
    s = BrowserRpcSession(

        # ja3="771,4865-4867-4866-49195-49199-52393-52392-49196-49200-49162-49161-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-34-18-51-43-13-45-28-27-65037,4588-29-23-24-25-256-257,0"
    )
    s.proxies = proxies
    # s.headers = {
    #     'Accept-Encoding': 'gzip, deflate, br',
    # }
    # ja3_json = s.get('https://tls.browserleaks.com/')
    # print(ja3_json.text)
    # if ja3_json:
    #     ja3_text = ja3_json.json()['ja3n_text']
    #     logger.info(ja3_text)
    #     logger.info('771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-5-10-11-16-17-23-35-13-43-45-50-51-65281,29-23-24-25-30-256-257-258-259-260,0')
    # s = Session(ja3='771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-5-10-11-16-17-23-35-13-43-45-50-51-65281,29-23-24-25-30-256-257-258-259-260,0',akamai='1:65536;2:0;4:6291456;6:262144|15663105|0|m,a,s,p')
    s.verify = False
    ts = int(time.time() * 1000)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0'
    # ip = "14.155.68.109"

    # ip = None
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua,
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    r = s.get('https://www.shenzhenair.com/szair_B2C/', headers=headers,proxies=proxies)
    print(s.cookies)
    headers_js = {
        'Host': 'www.shenzhenair.com',
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': ua,
        'Accept': '*/*',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://www.shenzhenair.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.shenzhenair.com/szair_B2C/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'ariauseGraymode=false; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219aaaa01f866e4-0ac6ca4373768b8-26061b51-2073600-19aaaa01f87ef3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219aaaa01f866e4-0ac6ca4373768b8-26061b51-2073600-19aaaa01f87ef3%22%7D',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    headers = {
        'Host': 'www.shenzhenair.com',
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://www.shenzhenair.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.shenzhenair.com/szair_B2C/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'AlteonP=AUwuXG9ADgoHvtoPgbSvXQ' + os.getenv('$', '') + '; HMF_CI=1e2ff28aa3d5bedc2f2226f97568fd9badcfc2260fcd8d81d387f452b3c33366632e5597ceed8f534c3457fd69c54d3c6993f5cda68bb2d5c786f13c550dd161fd; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ac358319412e0-0533076924cfa88-26061b51-2073600-19ac3583195a2e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac358319412e0-0533076924cfa88-26061b51-2073600-19ac3583195a2e%22%7D; ariauseGraymode=false',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {
        'plat': 'B2C',
    }

    response = s.post(
        'https://www.shenzhenair.com/szair_B2C/getHomePageData.action',
        params=params,
        headers=headers,
        proxies=proxies
    )
    logger.info(dict(response.cookies))
    r = s.get('https://www.shenzhenair.com/vodka/v1/dfp/bootstrap.js',headers=headers_js,proxies=proxies)
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.shenzhenair.com/szair_B2C/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": ua,

    }

    url = "https://www.shenzhenair.com/vodka/v1/bootstrap/param"
    params = {
        "t": ts
    }
    response = s.get(url, headers=headers, params=params,proxies=proxies)
    logger.info(response.text)
    logger.info(response.cookies)
    data_json = json.loads(response.text)
    x_s3_tid = data_json['_a'][0]
    x_s3_sid = data_json['_a'][1]
    r = s.get('https://www.shenzhenair.com/vodka/v1/js/sw.js',headers=headers_js,proxies=proxies)
    data = context.call('get_x_s3_s4e', x_s3_tid,x_s3_sid,ip,ua,None,None,fcp,cvp)
    pprint(data)
    x_s3_s4e = data['x_s3_s4e']
    s.cookies.set('x-s3-tid', x_s3_tid, domain='.shenzhenair.com', path='/')
    s.cookies.set('x-s3-s4e', x_s3_s4e,domain='.shenzhenair.com',path='/')
    s.cookies.set('fromPage','%7BfromPage%3A%22index%22%7D',domain='.shenzhenair.com',path='/')
    s.cookies.set('sccode','%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',domain='.shenzhenair.com',path='/')
    s.cookies.set('ariauseGraymode','false',domain='.shenzhenair.com',path='/')
    logger.info(s.cookies.get_dict())
    headers = {
        'Host': 'www.shenzhenair.com',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.shenzhenair.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.shenzhenair.com/szair_B2C/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'hcType': 'DC',
        'type': '单程',
        'orgCity': '深圳',
        'orgCityCode': 'SZX',
        'dstCity': '合肥',
        'dstCityCode': 'HFE',
        'orgDate': '2025-11-27',
        'dstDate': '2025-11-27',
        'quiz': [
            'Y',
            '1',
        ],
        'bzcPsgrName': '',
        'bzcCertNo': '',
    }

    response = s.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', headers=headers,proxies=proxies,data=data)
    logger.info(response.status_code)
    logger.info(response.text)

test()