import json

# import requests

import time
import execjs


from curl_cffi.requests.session import Session

s = Session(
    ja3="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-5-10-11-16-23-35-13-43-45-51-65281,29-23-24-25-256-257,0"
)


while True:
    ts = int(time.time() * 1000)
    print(ts)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
    }
    url = "http://api.tianqiip.com/getip"
    params = {
        "secret": "j6sjjczp",
        "num": "1",
        "type": "txt",
        "port": "1",
        "mr": "1",
        "sign": "91ac51fd3232c447486480bcb89d831f"
    }
    response = s.get(url, headers=headers, params=params,verify=False)
    proxy = response.text.strip()
    print(proxy)
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    url = "https://www.shenzhenair.com/szair_B2C/"
    response = s.get(url, headers=headers, proxies=proxies)
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://www.shenzhenair.com/vodka/v1/bootstrap/param"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.shenzhenair.com/szair_B2C/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    params = {
        "t": ts
    }
    response = s.get(url, headers=headers, params=params,proxies=proxies)
    data_json = json.loads(response.text)
    print('params',data_json)
    x_s3_tid = data_json['_a'][0]
    x_s3_sid = data_json['_a'][1]
    x_s3_s4e = execjs.compile(open('get_x_s3_s4e.js', 'r', encoding='utf-8').read()).call('get_x_s3_s4e', x_s3_tid, x_s3_sid,proxy)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.shenzhenair.com",
        "Pragma": "no-cache",
        "Referer": "https://www.shenzhenair.com/szair_B2C/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "arialoadData": "false",
        "x-s3-s4e":x_s3_s4e,
        "x-s3-tid":x_s3_tid,
        "fromPage": "%7BfromPage%3A%22index%22%7D",
        "sccode": "%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D",
        "ariauseGraymode": "false",
        # "sw_rtk":"Wxmz4n7ojgulTArnogiJe34aOizp"
    }
    for k,v in cookies.items():
        s.cookies.set(k,v,domain='.shenzhenair.com')
    print(s.cookies.get_dict())
    url = "https://www.shenzhenair.com/szair_B2C/flightSearch.action"
    data = {
        "condition.orgCityCode": "SZX",
        "condition.dstCityCode": "TFU",
        "condition.hcType": "DC",
        "condition.orgDate": "2025-11-24",
        "condition.dstDate": "2025-11-25"
    }
    response = s.post(url, headers=headers, data=data, proxies=proxies)
    print(response.status_code,response.text)
    time.sleep(2)