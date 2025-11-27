import json

import requests

import time
import execjs
from pprint import pprint
from loguru import logger



from curl_cffi.requests import Session
from curl_cffi  import ExtraFingerprints
import warnings
warnings.filterwarnings('ignore')
def test():
    fcp = 'c2331586'
    cvp = 'c8823e45'
    proxy = requests.get('http://api.tianqiip.com/getip?secret=u4kncdfw&num=1&type=txt&port=1&mr=1&sign=91ac51fd3232c447486480bcb89d831f').text.strip()
    print(proxy)
    ip_port = proxy.split(':')
    ip = ip_port[0]
    proxies = {
        'http':f'http://{proxy}',
        'https':f'http://{proxy}',
    }
    context = execjs.compile(open('get_x_s3_s4e.js', 'r', encoding='utf-8').read())
    ja3 = '771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,18-11-17613-0-10-35-13-16-5-65037-23-65281-45-43-27-51,4588-29-23-24,0'

    akamai_text="1:65536;2:0;4:6291456;6:262144|15663105|0|m,a,s,p"
    extra_fp = ExtraFingerprints(
        tls_grease=True,
        tls_signature_algorithms=[]
    )
    s = Session(akamai=akamai_text,impersonate='chrome142',proxies=proxies,http_version='v3',extra_fp=extra_fp)
    print(s.get('https://tls.browserleaks.com/').json()['ja3_text'])
    # s.proxies = proxies
    s.verify = False
    ts = int(time.time() * 1000)
    # ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0'
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
    r = s.get('https://www.shenzhenair.com/szair_B2C/', headers=headers)
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
    r = s.get('https://www.shenzhenair.com/vodka/v1/dfp/bootstrap.js',headers=headers_js)
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
    response = s.get(url, headers=headers, params=params)
    logger.info(response.text)
    logger.info(response.cookies)
    data_json = json.loads(response.text)
    x_s3_tid = data_json['_a'][0]
    x_s3_sid = data_json['_a'][1]
    r = s.get('https://www.shenzhenair.com/vodka/v1/js/sw.js',headers=headers_js)
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
    response = s.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', headers=headers,data=data)
    logger.info(response.status_code)
    logger.info(response.text)

test()