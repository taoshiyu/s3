import json

import requests

import time
import execjs



import requests
from requests import session
import warnings
warnings.filterwarnings('ignore')
def test():
    s = session()
    s.verify = False
    ts = int(time.time() * 1000)
    print(ts)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    ip = "38.87.67.154"
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

    r = s.get('https://www.shenzhenair.com/szair_B2C/', headers=headers, verify=False)
    print(s.cookies.get_dict())
    headers = {
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

    r = s.post('https://www.shenzhenair.com/szair_B2C/arithmeticCaptcha.action', headers=headers)
    print(r.cookies.get_dict())

    r = s.get('https://www.shenzhenair.com/vodka/v1/dfp/bootstrap.js')
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
    print(response.text)
    print(response.cookies.get_dict())
    data_json = json.loads(response.text)
    x_s3_tid = data_json['_a'][0]
    x_s3_sid = data_json['_a'][1]
    print(x_s3_tid)
    print(x_s3_sid)
    r = s.get('https://www.shenzhenair.com/vodka/v1/js/sw.js')
    data = execjs.compile(open('get_x_s3_s4e.js', 'r', encoding='utf-8').read()).call('get_x_s3_s4e', x_s3_tid,x_s3_sid,ip,ua,None,None)
    fp = data['fp']
    print(fp)
    x_s3_s4e = data['x_s3_s4e']
    print(x_s3_s4e)
    s.cookies.set('x-s3-sid', x_s3_sid,domain='.shenzhenair.com',path='/')
    s.cookies.set('x-s3-tid', x_s3_tid, domain='.shenzhenair.com', path='/')
    s.cookies.set('x-s3-s4e', x_s3_s4e,domain='.shenzhenair.com',path='/')
    # s.cookies.set('fromPage','%7BfromPage%3A%22index%22%7D',domain='.shenzhenair.com',path='/')
    # s.cookies.set('sccode','%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',domain='.shenzhenair.com',path='/')
    # s.cookies.set('ariauseGraymode','false',domain='.shenzhenair.com',path='/')
    print(s.cookies.get_dict())
    time.sleep(3)

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
    cookies = {
        'x-s3-sid':x_s3_sid,
        'x-s3-tid':x_s3_tid,
        'x-s3-s4e':x_s3_s4e
    }
    data = {
        'hcType': 'DC',
        'type': '单程',
        'orgCity': '深圳',
        'orgCityCode': 'SZX',
        'dstCity': '合肥',
        'dstCityCode': 'HFE',
        'orgDate': '2025-11-25',
        'dstDate': '2025-11-25',
        'quiz': [
            'Y',
            '1',
        ],
        'bzcPsgrName': '',
        'bzcCertNo': '',
    }

    response = s.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', headers=headers,cookies=cookies, data=data,verify=False)
    print(response.status_code, response.cookies.get_dict())

test()