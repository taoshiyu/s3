import json

import requests

import time
import execjs



import requests
from requests import session
def test():
    s = session()
    s.verify = False
    ts = int(time.time() * 1000)
    print(ts)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    ip = "120.229.99.37"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ua
    }
    url = "http://api.tianqiip.com/getip"
    params = {
        "secret": "a94lak1yr865z7ql",
        "num": "1",
        "type": "txt",
        "port": "1",
        "time": "10",
        "mr": "1",
        "sign": "91ac51fd3232c447486480bcb89d831f"
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    proxy = response.text.strip()
    print(proxy)
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
    print(r.status_code, s.cookies.get_dict())
    headers = {
        'Host': 'www.shenzhenair.com',
        'sec-ch-ua-platform': '"Windows"',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
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

    r = s.post('https://www.shenzhenair.com/szair_B2C/arithmeticCaptcha.action',
                             headers=headers)
    print(r.cookies.get_dict())


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
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
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
    x_s3_s4e = execjs.compile(open('get_x_s3_s4e.js', 'r', encoding='utf-8').read()).call('get_x_s3_s4e', x_s3_tid,x_s3_sid,ip,ua)
    print(x_s3_s4e)



    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.shenzhenair.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.shenzhenair.com/szair_B2C/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': ua,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'JSESSIONID=425AF37FA60D0045318C144596297BAE; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219a8fd299671166-040d7f2c718d538-26061b51-2073600-19a8fd29968188f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219a8fd299671166-040d7f2c718d538-26061b51-2073600-19a8fd29968188f%22%7D; x-s3-sid=S18jO3rksb91e344z4n7ojg2p; arialoadData=false; AlteonP=Acj5Om9ADgpYXDNpqZLcCA$$; sw_rtk=Wf4z4n7ojgdj5VxlacAKe344cM23; x-s3-s4e=dYA4ok%2BVAv0apopZQixNbzM73AisgazKhz8ZFf9liGCBJMqZyklGIzzFMBI9b0Lhceqqy0RWLLYAYglgEwcMMaTyy11vVwRVeiV1FtTvUqEn37rlgPhbOAb1psdWaGKFLlB5d73dN1CgjRDFcAoMOL1xzmLOPuchLPOTfK%2Bi63av3iqqKeCHyS7j8InYj4shFvpSiYSyZ63I4eztWO3W20Ci97qOa4xpmkta69j8VrDPpNi1BsYrAqzr4EvSPaKhruC7nDZ36POc%2FSPiG%2BkULtwfrQ5W61lvukYPcJmbGMVhHONXGomCL3Jk74BHPV7SOEYj%2BIVs%2B5%2FdzOBer3Ee4%2BT6chgtKlr9qSQeNXl3HGYaWuKvGJktks0mQpcaugUDundmFkE4P5ybHECNc9gIwqZIlbZCtEbsZ%2FjDyQFvF3Fg5VzdSQAnxB9z%2F45ye7xTB2JLIlBDH%2B9eUH7ZOBDMeudNhE5d4S6uDQY%2FIPixqanqrC%2BtCeEkT3aY%2F1%2FltGzXJLNfXWIMDpg%2BqSw7YBFTNpTnhMgLqE8mgIc4EZPqYZNg5VzdSQAnxB9z%2F45ye7xTBMVHF0PEVo9zWQLAX2SLhs%2Bcm47zxO1uSeUvMVULPAK%2FRhoBNPNVRtguj8vzylbBPUbY%2FoZnE4Ndc6AklszspZZapzHbxwqrtoqzco3R2oPqvHbSutMR1x7k6ccxJfPMLSTX59oZvuGSr7tF7lhp9CqQBgeHoK53jy%2BKcDWrEURewYiT8IyK0%2BCGVAVFnnRo%2BkCJqXsOs99UqVK7H4xIybuLxTS45X3faAXMPvayTXhRyeBpNN%2Bz5kh2hzAo8EpT3sSsbdbec2dfe035d78ed09097d73ac691ec55d08443:48:4a900515-c39e-11f0-a33d-3cd2e55daed6:6410012048; x-s3-tid=bdbec2dfe035d78ed09097d73ac691ec55d08443:48:4a900515-c39e-11f0-a33d-3cd2e55daed6:6410012048; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D; ariauseGraymode=false',
    }
    s.cookies.set('x_s3_tid', x_s3_tid,domain='.shenzhenair.com')
    s.cookies.set('x_s3_s4e', x_s3_s4e,domain='.shenzhenair.com')
    s.cookies.set('fromPage','%7BfromPage%3A%22index%22%7D',domain='.shenzhenair.com')
    s.cookies.set('sccode','%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',domain='.shenzhenair.com')
    s.cookies.set('ariauseGraymode','false',domain='.shenzhenair.com')
    print(s.cookies.get_dict())

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.shenzhenair.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.shenzhenair.com/szair_B2C/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'JSESSIONID=768759A74935A03846F54537C330D16A; AlteonP=AWLNQW9ADgorr8p6WzqtDQ$$; HMF_CI=dc6041d37d331e561a15cac2bb67571037dce1ea262c1cf7409456f2e49a82666fd40e9d35217afbb3b8dacdb2e4a8390a4be9f2e904256590616a4b2f0bb99c5e; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ab18e2e4210cf-0f9b381d4cd56a-26061b51-2073600-19ab18e2e431b80%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab18e2e4210cf-0f9b381d4cd56a-26061b51-2073600-19ab18e2e431b80%22%7D; arialoadData=false; x-s3-sid=S1q7lF2skmRHe34413lm9bazc; ariauseGraymode=false; x-s3-s4e=IF8kw9bemcjxFDrTBUuUdl6GlVA2YHpSogiiBnft5BIdDGYzleHJcwWoSqFxf4mU%2FJGWvFtVzCjK%2FSeWLmhKn0OVCGHwyZG43QfPBYFMDcO6yejmMp4YCUlJ2%2BFXmJMk8p%2BW%2BgD7Aje18cUGEDudVT12QhYux%2FVNQ2MLY82SFbh5f2p0WIqi9R3o7JIUfI%2BDAlOp2wxmvjWy9oAVq59GWNShNPSEQU0UtD15%2F2Z9ywr9T4w%2F%2BEAhCVmOtoLgJbi%2F6BacVLrNbAswYX9PHH8b%2FZtafS%2BkaZVPnYSnGJhL8syNEEOJAEFPCPx63faJCiCbETpoKwW%2B4i%2B%2FrhVhFqiZbUnCkVp%2B4juP7oQclVhEFsTh3xaYsGYhHz64O6H5Hfns2F47SnjfBBtzGZetB2L2H7QaWcJ%2FhDyS2ESjVr2bv%2BGWup05V6U8URwA9aGkpMKbaE0JhL2f8PFikC3n7%2FAh8XUqnfjmRBYDSh6eEHXZRhMh2Nnv7N20lXUqOpn7qIvmTaGsCdxm3qUBr1WDHfLFHwsFwj%2Flb8A%2BcxnI6Hf0VQzXmDowI%2FbwOHRPR%2FFhqbKwaE0JhL2f8PFikC3n7%2FAh8RhXJDLHY4Y3YpbRGavysO6aLUhRNTHjQOmw0%2BZ6KJfCTvB%2BGkzBIo2d9tLDHci3G09fUPBTE3hxeU2Znt%2FNVQZMrUJTUDWQZWJnOW%2FrB8JaTGTrqHL6a2PSjLOaRzPrPv73TBmipPm1V8a6xfXuAz4ktBT9b%2Bn43XdjAxC6pblRIogEWtvE8BZ%2B4uG2ogRwQvVHWPWOFAMr79JoVcGF6EyFvHs06jmz%2Fxa4Bf5ebetsfHSzO71DAclWSKOuIP5Ahg%3D%3D3sSs3d8fcd9c7e5a73b5ffe3a6dbb6c26ee13808ddf4:48:7c56e5d7-c88b-11f0-a33d-3cd2e55daed6:07998220f3; x-s3-tid=3d8fcd9c7e5a73b5ffe3a6dbb6c26ee13808ddf4:48:7c56e5d7-c88b-11f0-a33d-3cd2e55daed6:07998220f3; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
    }

    data = {
        'hcType': 'DC',
        'type': '单程',
        'orgCity': '深圳',
        'orgCityCode': 'SZX',
        'dstCity': '合肥',
        'dstCityCode': 'HFE',
        'orgDate': '2025-11-24',
        'dstDate': '2025-11-24',
        'quiz': [
            'Y',
            '1',
        ],
        'bzcPsgrName': '',
        'bzcCertNo': '',
    }

    response = s.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', headers=headers, data=data,verify=False)
    print(response.status_code, response.cookies.get_dict())


    url = "https://www.shenzhenair.com/szair_B2C/flightSearch.action"
    data = {
        "condition.orgCityCode": "SZX",
        "condition.dstCityCode": "HFE",
        "condition.hcType": "DC",
        "condition.orgDate": "2025-11-22",
        "condition.dstDate": "2025-11-22"
    }
    response = s.post(url, headers=headers, data=data, proxies=None)
    print(response.status_code)
    time.sleep(2)

test()