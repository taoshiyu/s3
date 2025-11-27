import execjs
import requests
from tls_client.sessions import Session
from loguru import logger
import time
domain = 'https://www.airkunming.com/'

def test():
    fcp = 'c2331586'
    cvp = 'c8823e45'
    # proxy = requests.get('http://api.tianqiip.com/getip?secret=j6sjjczp&num=1&type=txt&port=1&mr=1&sign=91ac51fd3232c447486480bcb89d831f').text.strip()
    # ip_port = proxy.split(':')
    # ip = ip_port[0]
    # print(ip)
    # # ip = None
    # proxies = {
    #     'http':f'http://{proxy}',
    #     'https': f'http://{proxy}'
    # }
    context = execjs.compile(open('get_x_s3_s4e.js', 'r', encoding='utf-8').read())
    s = Session(
        ja3_string='771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-5-10-11-16-17-23-35-13-43-45-50-51-65281,29-23-24-25-30-256-257-258-259-260,0',
        random_tls_extension_order=True,
        force_http1=True
    )
    ja3_json = s.get('https://tls.browserleaks.com/').json()
    if ja3_json:
        ja3_text = ja3_json['ja3n_text']
        logger.info(ja3_text)
        logger.info(
            '771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-5-10-11-16-17-23-35-13-43-45-50-51-65281,29-23-24-25-30-256-257-258-259-260,0')
    # s = Session(ja3='771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-5-10-11-16-17-23-35-13-43-45-50-51-65281,29-23-24-25-30-256-257-258-259-260,0',akamai='1:65536;2:0;4:6291456;6:262144|15663105|0|m,a,s,p')
    s.verify = False
    ts = int(time.time() * 1000)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0'
    ip = "14.155.68.109"

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

    r = s.get('https://www.airkunming.com/#/', headers=headers)
    print(s.cookies)
    headers_js = {
        'Host': 'www.shenzhenair.com',
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': ua,
        'Accept': '*/*',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://www.airkunming.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer':'https://www.airkunming.com/#/',
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
        'Origin': 'https://www.airkunming.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.airkunming.com/#/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'AlteonP=AUwuXG9ADgoHvtoPgbSvXQ' + os.getenv('$', '') + '; HMF_CI=1e2ff28aa3d5bedc2f2226f97568fd9badcfc2260fcd8d81d387f452b3c33366632e5597ceed8f534c3457fd69c54d3c6993f5cda68bb2d5c786f13c550dd161fd; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ac358319412e0-0533076924cfa88-26061b51-2073600-19ac3583195a2e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac358319412e0-0533076924cfa88-26061b51-2073600-19ac3583195a2e%22%7D; ariauseGraymode=false',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
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

    url = "https://www.airkunming.com/vodka/v1/bootstrap/param"
    params = {
        "t": ts
    }
    response = s.get(url, headers=headers, params=params)
    logger.info(response.text)
    logger.info(response.cookies)
    x_s3_tid = data_json['_a'][0]
    x_s3_sid = data_json['_a'][1]
    r = s.get('https://www.shenzhenair.com/vodka/v1/js/sw.js', headers=headers_js)
    data = context.call('get_x_s3_s4e', x_s3_tid, x_s3_sid, ip, ua, None, None, fcp, cvp)
    fp = data['fp']
    x_s3_s4e = data['x_s3_s4e']
    s.cookies.set('x-s3-tid', x_s3_tid, domain='.shenzhenair.com', path='/')
    s.cookies.set('x-s3-s4e', x_s3_s4e, domain='.shenzhenair.com', path='/')
    s.cookies.set('fromPage', '%7BfromPage%3A%22index%22%7D', domain='.shenzhenair.com', path='/')
    s.cookies.set('sccode', '%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D', domain='.shenzhenair.com', path='/')
    s.cookies.set('ariauseGraymode', 'false', domain='.shenzhenair.com', path='/')
    logger.info(s.cookies.get_dict())




    params_url = 'https://www.airkunming.com/vodka/v1/bootstrap/param?t=1764217479003'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.airkunming.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.airkunming.com/',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        # 'cookie': 'QINGCLOUDELB=bbe5cb4ba886e36034e7f77e5c0c32f47c2bf420413877967a5141d87db4f818; x-s3-sid=S1yeVxktbsXHe344z4nal7q1w; x-s3-tid=2740eefc5ef8cdcb4e3d817bf188ec27055c26fa:y2:82791a7e-cb48-11f0-bcf1-525401f1b7dd:ae97f52020; x-s3-sid=S1yeVxktbsXHe344z4nal7q1w; x-s3-s4e=jUaGWum%2BcNWw03H1A7z0j%2Bo21mLtcAQTCRhW6HJPs0v%2BkIqymLJHL3TDpPbQfCAFpU7SeKn5qSEQSbgRBydAl%2BPzInyt02SR4WASzMrEv4t6SpWfgiwnAaSd3tuKhxrR%2BH%2Byw8AjsMmASbOvab2n062iRkRX9X9dC4RA3xS4C3fbPN%2BP4FUmCJaooYO5ggktYNQah85e8%2FfXLBdyr3jBLVbg9b7eB9ZD9jY%2F3cEYCk%2F%2Bma4bzDaI0rWQjf3A13Cc%2B%2FuUWHorghAxzCy2V7ravUXtOWSNPgcjP29A6pMjiIQ6Bmme2H5Mmx1ER0E9%2Bq3G1AlH99crldCy2QnlmgU9MvXTURHSkRki1cWO2ho3VjeEv3sISUxy3hAbNuIGiSOFBZCATAP%2FNnexP%2BoGL8Wbb3BPG%2BeXo9%2F5oc%2BH82jbo5MdFVBFVH7rlJgloph0sNn6cAW0fKOyqQE5t0zSQG57KGCB2ZR5IboRjh4aopTn9RNPsvO0TgcGZKDf9UYw%2FrKPlYBHICF7ig6V2cfFLMd3XI2jarLZnS9mUv8paVYZ9pFTmi17tytLmyhykplQohYgkYLpqTViHG0w%2FJQz2jpTlTMOUx4rx9aZHecH2b80hnWv6ZfOPRCf4oRGoMAgQCQbkkUhjuaZ3RVM9R3BZvbSmIMOGNE5jHyYS45StBPHCctm%2Fy9ndGGBp7HgTQQrP7QUsBB6WJvz3mVg7cl3ozMM%2Fv%2BcAcNVRoBuWwczzlQhf3PjoG17NFEIKyzJrl2QWzCx7u%2F9AtKfukFpSGh5lmg49ytgO1RDjvKjuuC%2FAaVEp7Q%3D3sSsef0c366050c6748fdbb55f8edc3837ad8d7293f2:y2:8279318d-cb48-11f0-bb29-525401f1b7dd:08340320e2; x-s3-tid=ef0c366050c6748fdbb55f8edc3837ad8d7293f2:y2:8279318d-cb48-11f0-bb29-525401f1b7dd:08340320e2; sw_rtk=W7vz4nal7qvgOwvfcs1re344BJ3g',
    }

    json_data = {
        'memberId': '',
        'memberPhone': '',
        'tripType': 'OW',
        'passType': 0,
        'depAirportCode': 'KMG',
        'arrAirportCode': 'KWE',
        'depDate': '2025-11-27',
        'returnDate': '',
        'timestamp': 1764217287,
        'token': 'f8453faaa14f45279378d75efef77efc',
        'sign': 'VgN2SF5ltK8VFxQxfi5nH0VcgW3hGC2DMzrgY7sa1k6peiR1mCM20YljLt2TXTnOg//F2j1ORq74ePxE9ynzIkX4qO18mr3M75G5i4kLIETVDFSc6E24Ju5VCmv5feeiNbDgAOVPzO+i1vCs0ziQiGs74KQe67Ef/VDST4ZLgci/WLfuDJmm4p5Z6BJddNScXsg2uAZ+KZWuR1xgcZwksId5SNgJwIgAqLoxQ8w3V2w=',
    }

    response = requests.post('https://www.airkunming.com/search/flight', cookies=cookies, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"memberId":"","memberPhone":"","tripType":"OW","passType":0,"depAirportCode":"KMG","arrAirportCode":"KWE","depDate":"2025-11-27","returnDate":"","timestamp":1764217287,"token":"f8453faaa14f45279378d75efef77efc","sign":"VgN2SF5ltK8VFxQxfi5nH0VcgW3hGC2DMzrgY7sa1k6peiR1mCM20YljLt2TXTnOg//F2j1ORq74ePxE9ynzIkX4qO18mr3M75G5i4kLIETVDFSc6E24Ju5VCmv5feeiNbDgAOVPzO+i1vCs0ziQiGs74KQe67Ef/VDST4ZLgci/WLfuDJmm4p5Z6BJddNScXsg2uAZ+KZWuR1xgcZwksId5SNgJwIgAqLoxQ8w3V2w="}'
    #response = requests.post('https://www.airkunming.com/search/flight', cookies=cookies, headers=headers, data=data)