import json

import requests
import httpx

import time
import execjs
from curl_cffi.requests.session import Session
from pprint import pprint



import requests
from requests import session
from httpx import Client
import warnings
warnings.filterwarnings('ignore')
def test():
    fcp = '136ca139'
    cvp = 'b7a49df6'
    # proxy = requests.get('http://api.tianqiip.com/getip?secret=j6sjjczp&num=1&type=txt&port=1&mr=1&sign=91ac51fd3232c447486480bcb89d831f').text.strip()
    # ip_port = proxy.split(':')
    # ip = ip_port[0]
    # print(ip)
    # # ip = None
    # proxies = {
    #     'http':f'http://{proxy}',
    #     'https': f'http://{proxy}'
    # }
    proxies = None
    context = execjs.compile(open('get_x_s3_s4e.js', 'r', encoding='utf-8').read())
    s = Client(verify=False,http2=True)
    # s = Session(impersonate='firefox',akamai='1:65536;2:0;4:6291456;6:262144|15663105|0|m,a,s,p',ja3='771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-5-10-11-16-23-35-13-43-45-51-65281,29-23-24-25-256-257,0')
    s.proxies = proxies
    s.verify = False

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    ip = "120.229.99.37"

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

    r = s.get('https://www.shenzhenair.com/szair_B2C/', headers=headers)
    headers = {
        'Host': 'www.shenzhenair.com',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.shenzhenair.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.shenzhenair.com/szair_B2C/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'JSESSIONID=97DF6F0FAAF9B31645D7F9082A3C9DB1; AlteonP=AWFsOG9ADgqpnNEHNjdSKA' + os.getenv('$', '') + '; HMF_CI=43577111c53d46f317cfe295fc901ff7bbc356098cb9595941b328e4b8f93165ef12e88892b923f61c1adc8343bdf122a2425c56312f647389d789931c49b79ede; ariauseGraymode=false; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ac115701e0-0165b54d970da78-26061b51-2073600-19ac115701f16da%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac115701e0-0165b54d970da78-26061b51-2073600-19ac115701f16da%22%7D; arialoadData=false; x-s3-sid=S15qCv6cjrT9e34413lm9ba33; x-s3-s4e=rCl6Jbbz9OOpXp0qequyqYPuZd1egvAvn8OI3xfnE%2B0N4PKxaRvg6ZtaO%2BO1fwLa49Qyz%2F7GHTF%2F%2BlDSGwGOOaLbMDc1sIO9vBUY0EhShxwqEOsunGMdhLUfaRBTl4mvAq9%2FmaVorcHGZo4JsiXCjpEBjiVXb1T8zp8s6jQS0ZNxa8kaH6HITeoaHBtq1ZS62ojqzUtyeLUti0rqsHXCrQd1L8SXuu%2FauoE%2FYRNurOqStvjc4Rn80EqJY0CEAnztvIcipoy1U5KHUUmKXHsgIt92dksOeMNGbYhanfhCtEgD%2BrLZ%2F0jwlVJRV750UGJjSeAQ0PcvnXNBglfc2Fgi5hAnu%2BWePz7yTkD1ftbwOsqo6ispXP6R9WlWU7VpwHl8vxQ5kk53wjqY6GSHTGnBIYCsr2OPd4ptbGEtkBE2NIzhqlZLFBrp1idwRxhcm1I9cFxRhrpvU2wT5rmmeQN6L36jjgMVYdBrFG%2F%2FXVBVW%2FQqcQFXlvJLynMnptgX%2B1y7pzWYJV2f9VD3sjmaAafXWVCl7RW0u3y%2FT06oW%2FuVRwZbt1to7iN2uEHr9TzP9m6BcFxRhrpvU2wT5rmmeQN6LyxtnmaCLZ2tCKyfBYIGdTLdO%2BS%2Bc4uWqIx901qx0s6SwS8rAgY6MRGt%2BDSlmYToX2n7X3pMy%2FgMrpY9tqIoDHRF3NaXHmuDYxZLSbMZTyHqvgljT9oYK2MeH8KFZ7uG1vlrU5L7i5IiRqWtDkENP8sETMcBhJ6kjo3YJ%2BJ7Co2LGprMUelqqOw7QweL8HNS58hZMG64AxvvJeep2bJzRK1uF2AmpWXbYkIqVbY5g7zXHiVqUZxq9JsrXC%2BsAmwduA%3D%3D3sSs2cffc88fac96a6ee5b70f1e885951dfed24b5f9d:48:7019f913-cae8-11f0-a740-005056ae692b:8020c12089; x-s3-tid=2cffc88fac96a6ee5b70f1e885951dfed24b5f9d:48:7019f913-cae8-11f0-a740-005056ae692b:8020c12089; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
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
    # print(s.cookies.get_dict())
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
        'Accept': '*/*',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'Sec-Purpose': 'prefetch;prerender',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://www.shenzhenair.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.shenzhenair.com/szair_B2C/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'JSESSIONID=AD4C9826CD38FE58A27E4AEE3FCE9073; AlteonP=AU5mcG9ADgqus7cEMrztFg' + os.getenv('$', '') + '; HMF_CI=11a88eb09996b8fdcacee479e246628acbbca1aa8bf40182874ce1ca4ee5d93249e5dd2f0351a9ab8c85bc21834b4d5f3ddf444d31dd9abe865fd7efbc63bfac39; x-s3-sid=S16p7d50frD9e34413lm9ba1x; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ac0b2248d66a-0e8b3d55a7a29d-26061b51-2073600-19ac0b2248e1b9f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac0b2248d66a-0e8b3d55a7a29d-26061b51-2073600-19ac0b2248e1b9f%22%7D; arialoadData=false; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D; x-s3-s4e=qw90ctqRahKFJbIb4Zqp%2FLft3nGtc0y5vONZwtmOqN72IGvB%2B7k2u5YxW27KNUbPuW34mVrlkPGxtH0QfC9D15TxExsbXpvPVdig%2F54KRx1sYpX3rrMlZs7Hh3D9zR1X6vPC%2BbYL9qgD4JDSy3EBwIVj28jn8la7rAWAPlUk5NtxgUM6M03wAc9C%2Ft%2BmsZTpPEV3Wv3HqeL8Bht44yCm%2B7xZKubmaukIspqwXAGmYIu7gn3jWRJzwEK6jxCa3m6ee0uPEla%2Fx4pkmQtqIMA5KaxuLVo07f28sey7kmGZ7xv40OiO95LMRBOI%2FD5PZ9TMr%2Bo4Zq1C9rfMCB0ie7xMZiW4oqtAShFEH5E1PsdmET8iw9y9v0q3tb3pg8cn4G8F7oAacqyDBup8gjflN4MBus8djOmjaZ5XcJHtSfdpZf6GWH26Wlb7RmGxDKvcx%2Bccp608zh1vwpC7dL%2BeFRZSWCGZSpZrlDi287hOYv7xtmK43hKmA%2BPkd41BTzy9uoCY69XX3f1Sf6auQd9PquX98SnU1CUWhgehpKTH8eCIKKdbWQhkrinci7cxAEeyZs94p608zh1vwpC7dL%2BeFRZSWLcGZlX4A6SQV3M9mpFBcLZkQueDhsiQCL0ZSXfyPt5F0hg4qv%2FSbU5J%2F8Ehwm221iop1phfHewUvgs7qbX2JOhKYzVPSEnJsF%2FzF9pqcJS7pu%2BF1qlbsLlPpxOYPIXmzHFdorwQB%2BUGTjMynjA%2BCwEz81miuMJsUH0Gz%2BVw2nmbGT%2BGEbY%2FNXMl7wnI828B7%2B7LJ%2FSnYALoRvDwtwJStV%2BeDsOLRJXapChcYe4Ip4Cd59cIyHLRl1g72B6BEMnvvg%3D%3D3sSsc5b6ee4b9bbc2e3fae3d5c4572a8fa55d317a40b:48:b0ff747f-cada-11f0-a740-005056ae692b:2031c32082; x-s3-tid=c5b6ee4b9bbc2e3fae3d5c4572a8fa55d317a40b:48:b0ff747f-cada-11f0-a740-005056ae692b:2031c32082; ariauseGraymode=false',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = s.post('https://www.shenzhenair.com/szair_B2C/arithmeticCaptcha.action',
                             headers=headers)
    cookies = {
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219ac0abbd103d8-001cb847b5ba2c8-26061b51-2073600-19ac0abbd111e0f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac0abbd103d8-001cb847b5ba2c8-26061b51-2073600-19ac0abbd111e0f%22%7D',
        'ariauseGraymode': 'false',
        'arialoadData': 'false',
    }
    for k,v in cookies.items():
        s.cookies.set(k,v)

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
    ts = int(time.time() * 1000)
    url = "https://www.shenzhenair.com/vodka/v1/bootstrap/param"
    params = {
        "t": ts
    }
    response = s.get(url, headers=headers, params=params)
    print(response.text)
    # print(response.cookies.get_dict())
    data_json = json.loads(response.text)
    x_s3_tid = data_json['_a'][0]
    x_s3_sid = data_json['_a'][1]
    # s.cookies.set('x-s3-sid', x_s3_sid, domain='.shenzhenair.com', path='/')
    print(x_s3_tid)
    print(x_s3_sid)
    r = s.get('https://www.shenzhenair.com/vodka/v1/js/sw.js',headers=headers_js)
    random_str = context.call('_0x3ffcf8',4)
    random_str1 = context.call('_0x3ffcf8',4)
    # fp = [
    #     f'{x_s3_tid};{x_s3_sid}',
    #     ua,
    #     'zh-CN',
    #     '124.04347527516074',
    #     'Win32',
    #     [ip],
    #     nvp,
    #     ['1920', '1080', '1', '24'],
    #     -480,
    #     'https://www.shenzhenair.com/szair_B2C/',
    #     f'{random_str1}70e9495d8a8a2466dd5df8900ddeaa3c',
    #     cvp,
    #     '(https://www.shenzhenair.com/vodka/v1/js/sw.js:1:256343)\n',
    #     f'{random_str}c35b1b8f56f77ec57d5c1f0dfa817d61',
    #     [[2, 2, 2, 2, 2], [2, 2, 3, 2, 3, 3], 2, 2, 2, [3, 2, 3, 2, 2, 3], [2, 2, 2, 1, 1, 1, 3, 0], [2], [2], 2, [2],
    #      [2, 2], 2, 2], [], 2]
    fp = [
        "0924d00a39a2ae8fafd795e97ab61497a5da4593:48:dbeb1763-cad3-11f0-a33d-3cd2e55daed6:0c10c220cb;S1blFS1gdrFle34413lm9ba26",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "zh-CN", "124.04347527516074", "Win32", ["120.229.99.37"], "136ca139", ["1920", "1080", "1", "24"], -480,
        "https://www.shenzhenair.com/szair_B2C/", "79bdeb5270e9495d8a8a2466dd5df8900ddeaa3c", "b7a49df6",
        "(https://www.shenzhenair.com/vodka/v1/js/sw.js:5971:15)\n", "a1a153f0c35b1b8f56f77ec57d5c1f0dfa817d61",
        [[2, 2, 2, 2, 2], [2, 2, 3, 2, 3, 3], 2, 2, 2, [3, 2, 3, 2, 2, 3], [2, 2, 2, 1, 1, 1, 3, 0], [2], [2], 2, [2],
         [2, 2], 2, 2], [], 2]

    data = context.call('get_x_s3_s4e', x_s3_tid,x_s3_sid,ip,ua,None,None,fcp,cvp)

    pprint(data)
    fp = data['fp']
    print(json.dumps(fp))
    x_s3_s4e = data['x_s3_s4e']
    right_cookie = '6mRO97azy0JtLepEOE9X8jGmZbkDoalWH67Pm8SEE6bQGl9KdpIHrISWinUtPcNSmrj6%2BrC2AcQq2BK0gBgovZ8eqK2%2Be7JpvZKA8nkJVHcSYTUG0TgBdzOumQAopfjbUq4ZOgfYxi7y79IZFUjF6SNpEbjLgVRQNNJe7V8AYcaNNvHccaxmXE6wsuZ5vuDH6AOAh003U%2BFBLIVakp9bQyZ49H%2FKVO93UC2JBiDGGfvml2wED%2BrBamJSfgWZTZ9v8G9HcKqjzelmKIaB89tXUTSnKETe5imextj5zbpWX2G7eDMWt8JopvCu3p5HEnlczN2ram2Ddr%2FqpixHPN1ErmJkrFlY4u591IS%2Ba7ZptZuTCWZY4UkqIYqO1T99E5AqOlelnWlrBqYjkH83EPt0kk8TcGgVsTvbcQcVpknAdspxiC3S0lktiUKER0WbvPkxFYOeCNPnN7CrMR28ycSS6VKDYoDZci9MwDYouuuHbjaPPusEc87j%2BM%2BBhPpJbbwHXy16W6w8YtXHQf1l%2FXugeSW59x%2FO6aFNCZCEBPG36JK7ZI0N277yll45dcrDBRsNFYOeCNPnN7CrMR28ycSS6aeWkpfahw%2BuIoNlrt7w0cRRlnuCwwbff98QroC9arBWkYnYdKhkGGBV7MLUqttg%2FpmSaM2RW1WZvHbyF2aoAFq16McbdeLpAeXKzQfNfjXUMSq%2FwZYKLYTiOruB%2B43VFuJInEOk%2BZYQOAR9nvwEy8xyQ9fzDDMd5kFZQqGtvUyddaSvA2wp%2BgRyTeSntd068S1Yav%2FxkMdp0aBtudE11ZNICyvsvM5cSWOCWI8RfXfDfXDY9Tbz4yGWspK73D4YKA%3D%3D3sSs0924d00a39a2ae8fafd795e97ab61497a5da4593:48:dbeb1763-cad3-11f0-a33d-3cd2e55daed6:0c10c220cb'
    print(x_s3_s4e==right_cookie)
    s.cookies.set('x-s3-s4e', x_s3_s4e, domain='.shenzhenair.com', path='/')
    s.cookies.set('x-s3-tid', x_s3_tid, domain='.shenzhenair.com', path='/')
    s.cookies.set('fromPage','%7BfromPage%3A%22index%22%7D',domain='.shenzhenair.com',path='/')
    s.cookies.set('sccode','%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',domain='.shenzhenair.com',path='/')
    # cookies = {
    #     'x-s3-sid':x_s3_sid,
    #     'x-s3-s4e':x_s3_s4e,
    #     'x-s3-tid':x_s3_tid
    # }
    # s.cookies.set('ariauseGraymode','false',domain='.shenzhenair.com',path='/')
    print(dict(s.cookies))
    time.sleep(3)

    cookies = {
        'JSESSIONID': s.cookies.get('JSESSIONID'),
        'AlteonP': s.cookies.get('AlteonP'),
        'HMF_CI': s.cookies.get('HMF_CI'),
        'ariauseGraymode': 'false',
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219ac115701e0-0165b54d970da78-26061b51-2073600-19ac115701f16da%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac115701e0-0165b54d970da78-26061b51-2073600-19ac115701f16da%22%7D',
        'arialoadData': 'false',
        'x-s3-sid': s.cookies.get('x-s3-sid'),
        'x-s3-s4e': s.cookies.get('x-s3-s4e'),
        'x-s3-tid': s.cookies.get('x-s3-tid'),
        'fromPage': '%7BfromPage%3A%22index%22%7D',
        'sccode': '%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
    }

    headers = {
        'Host': 'www.shenzhenair.com',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.shenzhenair.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.shenzhenair.com/szair_B2C/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'JSESSIONID=97DF6F0FAAF9B31645D7F9082A3C9DB1; AlteonP=AWFsOG9ADgqpnNEHNjdSKA' + os.getenv('$', '') + '; HMF_CI=43577111c53d46f317cfe295fc901ff7bbc356098cb9595941b328e4b8f93165ef12e88892b923f61c1adc8343bdf122a2425c56312f647389d789931c49b79ede; ariauseGraymode=false; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ac115701e0-0165b54d970da78-26061b51-2073600-19ac115701f16da%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac115701e0-0165b54d970da78-26061b51-2073600-19ac115701f16da%22%7D; arialoadData=false; x-s3-sid=S15qCv6cjrT9e34413lm9ba33; x-s3-s4e=rCl6Jbbz9OOpXp0qequyqYPuZd1egvAvn8OI3xfnE%2B0N4PKxaRvg6ZtaO%2BO1fwLa49Qyz%2F7GHTF%2F%2BlDSGwGOOaLbMDc1sIO9vBUY0EhShxwqEOsunGMdhLUfaRBTl4mvAq9%2FmaVorcHGZo4JsiXCjpEBjiVXb1T8zp8s6jQS0ZNxa8kaH6HITeoaHBtq1ZS62ojqzUtyeLUti0rqsHXCrQd1L8SXuu%2FauoE%2FYRNurOqStvjc4Rn80EqJY0CEAnztvIcipoy1U5KHUUmKXHsgIt92dksOeMNGbYhanfhCtEgD%2BrLZ%2F0jwlVJRV750UGJjSeAQ0PcvnXNBglfc2Fgi5hAnu%2BWePz7yTkD1ftbwOsqo6ispXP6R9WlWU7VpwHl8vxQ5kk53wjqY6GSHTGnBIYCsr2OPd4ptbGEtkBE2NIzhqlZLFBrp1idwRxhcm1I9cFxRhrpvU2wT5rmmeQN6L36jjgMVYdBrFG%2F%2FXVBVW%2FQqcQFXlvJLynMnptgX%2B1y7pzWYJV2f9VD3sjmaAafXWVCl7RW0u3y%2FT06oW%2FuVRwZbt1to7iN2uEHr9TzP9m6BcFxRhrpvU2wT5rmmeQN6LyxtnmaCLZ2tCKyfBYIGdTLdO%2BS%2Bc4uWqIx901qx0s6SwS8rAgY6MRGt%2BDSlmYToX2n7X3pMy%2FgMrpY9tqIoDHRF3NaXHmuDYxZLSbMZTyHqvgljT9oYK2MeH8KFZ7uG1vlrU5L7i5IiRqWtDkENP8sETMcBhJ6kjo3YJ%2BJ7Co2LGprMUelqqOw7QweL8HNS58hZMG64AxvvJeep2bJzRK1uF2AmpWXbYkIqVbY5g7zXHiVqUZxq9JsrXC%2BsAmwduA%3D%3D3sSs2cffc88fac96a6ee5b70f1e885951dfed24b5f9d:48:7019f913-cae8-11f0-a740-005056ae692b:8020c12089; x-s3-tid=2cffc88fac96a6ee5b70f1e885951dfed24b5f9d:48:7019f913-cae8-11f0-a740-005056ae692b:8020c12089; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'hcType': 'DC',
        'type': '单程',
        'orgCity': '深圳',
        'orgCityCode': 'SZX',
        'dstCity': '合肥',
        'dstCityCode': 'HFE',
        'orgDate': '2025-11-26',
        'dstDate': '2025-11-26',
        'quiz': [
            'Y',
            '1',
        ],
        'bzcPsgrName': '',
        'bzcCertNo': '',
    }

    response = requests.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', cookies=cookies, headers=headers,
                  data=data)
    print(response.status_code)

test()