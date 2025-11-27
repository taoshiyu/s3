import json

import requests

import time
import execjs
from pprint import pprint
from loguru import logger
import re


from curl_cffi.requests import Session
from curl_cffi  import ExtraFingerprints
import warnings
warnings.filterwarnings('ignore')
import random


def parse_params_url(t):
    match = re.search(r'_bs_ctl_param_url\s*=\s*(.*?),',t)
    if match:
        return match.group(1)
    else:
        return None


def get_boot_strip_source(html):
    src_match = re.search(r'src="/vodka/v1/dfp/bootstrap.js(.*?)"',html)
    if src_match:
        src_str = src_match.group(1)
        if src_str:
            source_match = re.search(r'(?:^|[&])source=([^&]+)',src_str)
            if source_match:
                return source_match.group(1)
    return ''


def get_rtk(params):
    rtk = params['_a'][2]
    return rtk

def get_params_params(html_text):
    if 'sw_3d81e4f25a8883b9308380ca68466a56' in  html_text:
        pass


def get_params(session,html_text):

    pass

def search_flight(session,ua):
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
    response = session.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', headers=headers, data=data)
    if response.status_code == 200:
        logger.info('成功')
        logger.info(response.cookies)
        logger.info(session.cookies.get_dict())
        headers = {
            'Host': 'www.shenzhenair.com',
            'sec-ch-ua-platform': '"Windows"',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': ua,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-ch-ua-mobile': '?0',
            'Origin': 'https://www.shenzhenair.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.shenzhenair.com/szair_B2C/flightsearch.action',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cookie': 'JSESSIONID=E4507A3B2F4E6531A59D4CE677D92D84; HMF_CI=98df2d903c72ffbb69a6f92607fa4e6d651724bb9fc9acb67134f098dbc355309dbc01d3b194461f7f431d48bb22198ea824ff1dda523bc991a3a8dcf38baf4067; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ac15e102f1f51-0d5b712d3eaf9a8-26061b51-2073600-19ac15e10301086%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac15e102f1f51-0d5b712d3eaf9a8-26061b51-2073600-19ac15e10301086%22%7D; x-s3-sid=S1esvxxhmrRte34413lm9bazc; arialoadData=false; sw_rtk=WW313lm9baitKn3l6tR9e3447b3e; x-s3-s4e=Bo2DHNxUY6bQlAZQBbDuThn9oQ7Zrmwyrc3ZAnFpw60292lyW8W1I19178V8nxl25Nv0rSdpg16WBWuwvX1NAX3EsQXlAGTUytVGcI0LSChxPE5sDBex83D6bfPidTgD6Za39gRDXfmLe2bd0WoYuYMR7mEQGvXsCXg6u%2BUO2AaY06OilVwg2r6wiQtLevgIi%2BDsmvB3mSlNOS3p8sevw8HDjBXEHnNFcRoJz8dOybQkTPotHS5eyuJe%2BclDkTt9jZOXda%2Fj0u1GMoObwaiNNlsRyQUEOrNsyycaMdfdyuJXR3A8JS0Bk5rWNRbnSM9rF%2BJeEtDMOt4CJxqkOgl2iL5E3MJxN%2BnpnP4LClK%2Fn6%2FObVcJDWhImx80%2FrX1wH8JgYLap90SiJf%2F366YRHPvDEweg%2Bzx%2FgkD7kI9iYEhMT%2BLy2caMxD541msenlz65mUilcXQlGmuCiPlABaaqcztI%2FJATQpdcqunvFYh03vugmH9cLf2hOCB%2BFgkZ9%2FRzG5Nu25wf6Swgz7q9sAM1F1iIuE7q7HyC7qpxKZrEaw9g2mIOXopUxECP9w7wNsJxNMilcXQlGmuCiPlABaaqcztPHq5geRKkLTbepE9x5mC98xmIan92e%2B%2BLUpxDSc43eGmrwbTEeHRpCU08QqcYG4mGVlK0YaRK10j1itjU7R7eWHjyAFuNaXwO9e213SJfd8DKdyFeLADQcEtP%2Bh5%2B4BU2UetIGgiTQY3adcjGMGcVCvFsyO6h704FHjHGqgByfJ%2FekbHT1OHbBJUp5zt8tmKcrwwftiZlM8bChL0ELF7JfOFLDPDlGmV1NToUZMRwilEU71wsOXUdjZuhDzPTR6JA%3D%3D3sSsc843cbca809d97273a47bb0accda6059c8d15610:48:19408e6e-cbaf-11f0-a33d-3cd2e55daed6:0020402094; x-s3-tid=c843cbca809d97273a47bb0accda6059c8d15610:48:19408e6e-cbaf-11f0-a33d-3cd2e55daed6:0020402094; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D; AlteonP=ACBHUW9ADgr+ZtsB4r5DNg' + os.getenv('$', '') + '; ariauseGraymode=false',
        }

        data = {
            'condition.orgCityCode': 'SZX',
            'condition.dstCityCode': 'HFE',
            'condition.hcType': 'DC',
            'condition.orgDate': '2025-11-28',
            'condition.dstDate': '2025-11-28',
        }

        response = session.post('https://www.shenzhenair.com/szair_B2C/flightSearch.action',headers=headers, data=data)
        if response.status_code == 200:

            print(response.json())
    else:
        logger.info(response.status_code)
        logger.info(response.headers)
        logger.info(response.text)






def test():
    fcp = '136ca139'
    # fcp = '123fsdff'
    cvp = 'b7a49df6'
    # cvp = 'b7sd9df6'
    fcp = 'c2331586'
    cvp = 'c8823e45'
    proxy = requests.get('http://api.tianqiip.com/getip?secret=j6sjjczp&num=1&type=txt&port=1&mr=1&sign=91ac51fd3232c447486480bcb89d831f').text.strip()
    print(proxy)
    ip_port = proxy.split(':')
    # ip = ip_port[0]
    ip = None
    proxies = {
        'http':f'http://{proxy}',
        'https':f'http://{proxy}',
    }
    fp = ["a9948d2aa9cd6ec48b9a0260a43452062d8f5475:48:958d034d-cb9c-11f0-a33d-3cd2e55daed6:03ee0220fc;S1lqOgrv0tr4e34413lm9baze","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36","zh-CN","124.04347527516074","Win32",["120.229.99.37"],"136ca139",["1920","1080","1","24"],-480,"https://www.shenzhenair.com/szair_B2C/","17b6f5bc70e9495d8a8a2466dd5df8900ddeaa3c","b7a49df6","(https://www.shenzhenair.com/vodka/v1/js/sw.js:5971:15)\n","43973898c35b1b8f56f77ec57d5c1f0dfa817d61",[[2,2,2,2,2],[2,2,3,2,3,3],2,2,2,[3,2,3,2,2,3],[2,2,2,1,1,1,3,0],[2],[2],2,[2],[2,2],2,2],[],2]

    ip = '120.229.99.37'
    context = execjs.compile(open('get_x_s3_s4e.js', 'r', encoding='utf-8').read())
    ciphers = '18-11-17613-0-10-35-13-16-5-65037-23-65281-45-43-27-51'.split('-')
    random.shuffle(ciphers)
    print(ciphers)
    ja3 = f'771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,{'-'.join(ciphers)},4588-29-23-24,0'

    akamai_text="1:65536;2:0;4:6291456;6:262144|15663105|0|m,a,s,p"
    extra_fp = ExtraFingerprints(
        tls_grease=True,
        tls_signature_algorithms=[]
    )
    s = Session(akamai=akamai_text,ja3=ja3,allow_redirects=False,proxies=proxies)
    # s.cookies.set('x-s3-sid','S1esvxxhmrRte34413lm9bazc',domain='.shenzhenair.com',path='/')
    # s.cookies.set('x-s3-s4e','w8mzWHv5z77Ef%2Ft22UwRL6qB3olpw02xtrRAyM%2F%2BpI%2BZetQPslKLRpl5EtQJ%2BTnih7SpG95QzZx7CuTWetmzF3drEVikj%2B9zHQm7VoixfnMNHD5q1%2FyG5uHWKc80jEFmiDiMu2HQ9xdYZkPVPzRr705Q3oLD5e6WRz%2FCIM58X2C6PTxLmrAbLxd1e5RefbBH067Wogvt9Qd%2FoxQ5dI4C5QhnfdUBrIGok5M%2BaO1zJ6Ubve7sVpSI2oFtMOXKhwBvmc%2FLdR0BhhzIhLEs6sHVDa5nZk901mhI%2BNy7TbE5ji4xBofq0Zb0LMEfJeOeY64UWkL1P%2BYU%2FCDNb25rGwbS9Y%2Ba89DGo1gCPn2hEN3FFKU5gk9n%2BH4dfN1HPEVB5%2BaYZo6EOUMBULhLpaUJ4gzQoXt6POWao3hoo04Kd6vLq1PF7NujUXefRP6FgeCaQFfuR4FL6%2BZJCp5986YXYDL6O2uXBxThVuDJqNmPMPc1ckneOPtXMoz1xAEVQdUyY7evNOjmqGv7HbubYM6ACGW2Vkt7BjEdwVxr4%2FYZKQJE8wEMYommqeIP3LtWSYXMyNpKR4FL6%2BZJCp5986YXYDL6O601gQaT5DVv5ITwnlTgYyykqediwKyc5L0QaYZlWDtRW3c5Ha%2BRqqE1MtlYAqSwRrQXYoc0miW34wf4hlWvVOkpqEmieECBvfesbkNgeILNC%2B5JyIUKNEY1iLrhrRslelGb0ezK3aZFyFdOamb6hHu7Kc083aEusdrGbJHie5qB6IrEz4sA5pCTuaOq%2FOnUzym%2B2lBY5ik6KcFVj%2Bbph8%2Fb%2Fqc%2FW%2BRXu16b7Rxs3rvVLfPW%2FIW6WXfrMA81yCc48Q%3D%3D3sSsed9fca8cf14b05d4ccb806fb033f297932e68eb0:48:2c69409b-cbb4-11f0-a33d-3cd2e55daed6:00164220bc',domain='.shenzhenair.com',path='/')
    # s.cookies.set('JSSESSIONID','2EE6D12BF096A378A7B6EB186F80F251',domain='www.shenzhenair.com',path='/szair_B2C/')
    print(s.get('https://tls.browserleaks.com/').json()['ja3_text'])
    # s.proxies = proxies
    s.verify = False

    # ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0'

    ua = random.choice([
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    ])
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
    with open('szair.html','w',encoding='utf-8') as f:
        f.write(r.content.decode('utf-8'))
    boot_strip_source=get_boot_strip_source(r.text)
    logger.debug("boot_strip_source={}".format(boot_strip_source))
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
        'User-Agent': ua,
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
    )
    logger.info(dict(response.cookies))
    # r = s.get('https://www.shenzhenair.com/vodka/v1/dfp/bootstrap.js',headers=headers_js)
    # params_url = parse_params_url(r.text)
    # with open('bootstrap.js', 'w') as f:
    #     f.write(r.text)
    # logger.debug(f'params_url={params_url}')
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
    ts = int(time.time() * 1000)
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
    # x_s3_sid = context.call('get_random_sid')
    # x_s3_tid = context.call('get_random_tid')
    # s.cookies.set('x-s3-sid', x_s3_sid, domain='.shenzhenair.com', path='/')
    # s.cookies.set('x-s3-tid', x_s3_tid, domain='.shenzhenair.com', path='/')
    data = context.call('get_x_s3_s4e', x_s3_tid,x_s3_sid,ip,ua,None,None,fcp,cvp)
    pprint(data)
    x_s3_s4e = data['x_s3_s4e']

    s.cookies.set('x-s3-tid', x_s3_tid, domain='.shenzhenair.com', path='/')
    s.cookies.set('x-s3-s4e', x_s3_s4e,domain='.shenzhenair.com',path='/')
    s.cookies.set('fromPage','%7BfromPage%3A%22index%22%7D',domain='.shenzhenair.com',path='/')
    s.cookies.set('sccode','%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',domain='.shenzhenair.com',path='/')
    s.cookies.set('ariauseGraymode','false',domain='.shenzhenair.com',path='/')
    logger.info(s.cookies.get_dict())
    search_flight(s,ua)

test()