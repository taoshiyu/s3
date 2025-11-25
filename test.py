import os
import requests


import execjs

js_str = open('./get_x_s3_s4e.js').read()
context = execjs.compile(js_str)
fp = ["b96a1e2fcb7a436ac242fc4e5b101716973b521f:48:23b871d0-c8ff-11f0-a33d-3cd2e55daed6:08206d20db;S1apfZj8inCWe344z4naowp1u","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36","zh-CN","124.04347527516074","Win32",["38.87.67.251"],"c2331586",["1920","1080","1","24"],-480,"https://www.shenzhenair.com/szair_B2C/","417985b62f65cb467a16e4ea8de74c2d14d2d0cf","c8823e45","(https://www.shenzhenair.com/vodka/v1/js/sw.js:1:256343)\n","f249f6811d0103ce77ba72408a64f6db5ca210bc",[[2,2,2,2,2],[2,2,3,2,3,3],2,2,2,[3,2,3,2,2,3],[2,2,2,1,1,1,3,0],[2],[2],2,[2],[2,2],2,2],[],2]
x_s3_tid,x_s3_sid = fp[0].split(';')
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
ip = '38.87.67.251'
x_s3_s4e = context.call('get_x_s3_s4e',x_s3_tid, x_s3_sid,ip,ua,None,fp)
print(x_s3_s4e)

cookies =  {
    'JSESSIONID': '83D5E27DC591EA4D5227459424296D7D',
    'AlteonP': 'AcO8B29ADgqJvMtzqoasVg$$',
    'HMF_CI': 'a6ffdb81aa62d037a66373eb62e1add35f8abd5dd6f294d4356734e3bd117961bcba728428caa758c959841bef8a3bcac3e55ecb3fb9aabab18ef539032e41d470',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219ab47671322f8-07ca3e197847b28-26061b51-2073600-19ab4767133127c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab47671322f8-07ca3e197847b28-26061b51-2073600-19ab4767133127c%22%7D',
    'arialoadData': 'false',
    'x-s3-sid': x_s3_sid,
    'sw_rtk': 'Wiez4naowpsja9npin4ue344LAz0',
    'ariauseGraymode': 'false',
    'x_s3_s4e':x_s3_s4e,
    'x-s3-tid': x_s3_tid,
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
    # 'Cookie': 'JSESSIONID=D1CDB3692E87C2BB051909E8B17A3275; AlteonP=A1CbQm9ADgoTQjUIHTQWJg' + os.getenv('$', '') + '; HMF_CI=dc0ef7d54da0dc5613bd7236a2bb7516c5c362f532d47f2fc60dd7c5ba043d37ee7a2bfa855dff11f1edc6eb2a1b2e96eedcc9a357e4236f8b002d60a33344764c; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ab3ffb44dc55-0cde96db35cf98-26061b51-2073600-19ab3ffb44ec21%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab3ffb44dc55-0cde96db35cf98-26061b51-2073600-19ab3ffb44ec21%22%7D; arialoadData=false; x-s3-sid=S14d5y12dnhFe344z4naowpzm; sw_rtk=WmSz4naowpeb3Jmgdn6Fe344x32t; ariauseGraymode=false; x-s3-s4e=os6BR%2FiMtv7gXnckVokXrat9iAkfQ%2BC6ldlTyOE8SqQDyr9GRbKID2Khn0Ut7ghi2L%2Fv6ptRS9TcoD0LVf6%2BCYWJjeMKVZcBcZDQfn3JW10vDo0BrN6TjT8BaRz3BhDPoum9OejfnnMrHXwPiS1HiQDICk%2FcERoOvp39XkSB%2FOKAHYwKyqfAeWP1cexTtJfqwq5xJ4m3zUwPR%2FMiclUbNlPG4719u3upDm9u0BmRDpCENHnHX2FtEu8brGzFf4iO1UtyYQGdpp4w7%2FNnsNwcLfAIuzBDNuRhwal%2BddoxYqpiURPNZe6OR2qLBdq1dSGBk%2FwvNxGUt%2FReBuQY5322OlVkR9qcoSass1IvNiCqwUcPDIetrgj7YWNqW5XCmqynreAocTH2%2FSsJ9%2F3z0qT3WIl2Nafg0rr2BS48FlbX7XzL%2BV4RTeeR4qfKCX0TeEtUz%2Fe4kERXbjST99uVBIfoYABaFKzmSkhb6Vl70hNw6%2BXHC19WQZvfoncy8IFN15DBGEt5rRexowunbIhfdfWD%2Fzs4o7lDSYHO%2Bof7BEKMMrhR76pFnx%2Feo%2Fvn415nOJ1Gz%2Fe4kERXbjST99uVBIfoYEEmhLi4PeH8ETYr9x4sJPQwDuDL8r8ewjz%2FcVyYMEZ2caJfivtXCxfwZldk2Ugew1b8rtxv4mEdkhsH23Ho0SyB8Ewq35UDPLcfW2NAvj0w%2BfeJu3Cd4u44o6u6R%2FTvYTL4Khgz91CW4Q5PyDsvpGBW6vW2Ib1JNo84WKynOuYMJjvwPp5BTkQ%2Fept2oMfnHh2tA4mk0ZPdIZJX84MhQfXCi6RN27jaIKALoQls0c3lM3tXyamvaWLCgrkYLo1a7A%3D%3D3sSs90b963c680e6c96bdc173fd83526e60642be1200:48:66b38f51-c8e9-11f0-a33d-3cd2e55daed6:0c008220c9; x-s3-tid=90b963c680e6c96bdc173fd83526e60642be1200:48:66b38f51-c8e9-11f0-a33d-3cd2e55daed6:0c008220c9; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
    'Content-Type': 'application/x-www-form-urlencoded',
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

response = requests.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', cookies=cookies, headers=headers, data=data)
print(response.status_code)
print(response.text)