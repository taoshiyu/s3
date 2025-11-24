import os
import requests
import execjs
with open('./get_x_s3_s4e.js') as f:
    js_str = f.read()

context  = execjs.compile(js_str)
fp = ["03d28a22bb54ab07959b21a19e80263503d97a1e:48:e101f342-c949-11f0-a33d-3cd2e55daed6:7810c02058;S18epxdo5oMWe34413lm9ba10","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36","zh-CN","124.04347527516074","Win32",["120.229.99.37"],"136ca139",["1920","1080","1","24"],-480,"https://www.shenzhenair.com/szair_B2C/","d6078b5b70e9495d8a8a2466dd5df8900ddeaa3c","b7a49df6","(https://www.shenzhenair.com/vodka/v1/js/sw.js:1:256343)\n","726434b6c35b1b8f56f77ec57d5c1f0dfa817d61",[[2,2,2,2,2],[2,2,3,2,3,3],2,2,2,[3,2,3,2,2,3],[2,2,2,1,1,1,3,0],[2],[2],2,[2],[2,2],2,2],[],2]
id_parts = fp[0].split(';')
x_s3_tid = id_parts[0]
x_s3_sid = id_parts[1]
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
ip = "120.229.99.37"
x_s3_s4e = context.call('get_x_s3_s4e', x_s3_tid, x_s3_sid,ua,ip,None,None)


cookies = {
    'JSESSIONID': 'AD11518E77971D0696794795E625A656',
    'AlteonP': 'A9RmBG9ADgqFFpUf7ANlIw$$',
    'HMF_CI': '82f3cec570a0f5c99ba8ff4f77522d00d88aa6e40b868d5273869b24ab00b537427201e70b9422b1297fce414322f492ef4430c1c09b0a8dba980076ea0e491a60',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219ab6788f1c1154-080a9e7d9b08c88-26061b51-2073600-19ab6788f1d2062%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab6788f1c1154-080a9e7d9b08c88-26061b51-2073600-19ab6788f1d2062%22%7D',
    'ariauseGraymode': 'false',
    'arialoadData': 'false',
    'x-s3-sid': 'S18epxdo5oMWe34413lm9ba10',
    'x-s3-s4e': 'HLNJniHpRngKIRpjKNZmFNTJkEYL%2BU56Bqt2ZA8XTnRuq5%2Fuv5vjPBk5oZ9Vo%2FqtM9BUJ%2BlR3jARcesGPAV6Wd5PY5J31terPV3yFvNUkIUquyEBVb3hK6bCdOtogOxT8lOLRIeEcGRCq2xPGnclSeFwvmp1JpjEgzRZ007oIB%2Bzxbt0T0NqQpVCrfJ7YKa4cZwaejln8v2asCEVhvKQCwdQU28UWQUfIZ4kmTUIgtsX44UTFNSvSwnrDKWBr51jXG7yMRw540VDjlaiSOWQ1R9YD4lAvvnmu5FrI3LpkJ8sEZMw60Owgqb3Bnl8dw0HwNvqw1UanaBgUSzshxNmty1aGGZdms0drvsQ7se1g1YlXROeRPV%2Fqn%2FQRsEko6Y5vpBpuNXhzqkRnzF%2FPK5uDgZ19PUDF1h7lRIWtmbNfU8TuAvPsDGtXdPkurdCtKujEGFXMn%2FIiiTTDj%2FGENAF6bS8sntpnV%2B82ftgVs9SffCK2kYLnKKDlqTDsy87r%2B0CN86hsCuaj%2FKmvmFX9KhCyf7kForLGkup%2Fle92Z6FY7EaT27WL3BPEfH9sgcK7yieEGFXMn%2FIiiTTDj%2FGENAF6f%2BrUoZe61e7BKhbuS6rvOpyVFDDsoVTuAJWS7f2z03i7WBH6bxtGF6P7ddyodfgg2L6iWFbE862qSBGvK6Wi3v6B5BMaSSHbwulYabdhhvjsjr%2BUQ%2BWJ%2FeRgMgTLcwJuwy2mpdCc6vyt9Kf7HVJ96FMVWSFtw%2Bzyul14PMHlERSpGp%2BmCoyRDdkvIuI%2Fgand7aaaXEE59njhkYZQno3CGVEVhLuCw%2BKflNiCqvHKDYnEdOkaNV9X2rvX5eeArfUXg%3D%3D3sSs03d28a22bb54ab07959b21a19e80263503d97a1e:48:e101f342-c949-11f0-a33d-3cd2e55daed6:7810c02058',
    'x-s3-tid': '03d28a22bb54ab07959b21a19e80263503d97a1e:48:e101f342-c949-11f0-a33d-3cd2e55daed6:7810c02058',
    'fromPage': '%7BfromPage%3A%22index%22%7D',
    'sccode': '%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
}
print(x_s3_s4e)
print(cookies['x-s3-s4e'])
print(cookies['x-s3-s4e']==x_s3_s4e)
cookies.update(
    {
    'x-s3-sid': x_s3_sid,
    'x-s3-s4e':x_s3_s4e,
    'x-s3-tid': x_s3_tid,
    }
)



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
    # 'Cookie': 'JSESSIONID=699B25C5874EA183F17305A2025EF807; AlteonP=AfVlNG9ADgrlvrgHsGdZKQ' + os.getenv('$', '') + '; HMF_CI=57c851f31db19ca333ebb569a35fc95bffc08b9e2af07277c44da9949237aa36b60453bb8400786f2b20bc246c133d89d03eed6127cc45e50e70c8e3934c419ae8; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ab669515d59a-01a0ab3ee3af4f8-26061b51-2073600-19ab669515e1d20%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab669515d59a-01a0ab3ee3af4f8-26061b51-2073600-19ab669515e1d20%22%7D; ariauseGraymode=false; arialoadData=false; x-s3-sid=S1dtaA015ophe34413lm9ba28; x-s3-s4e=5A2Z540pUVMEDbibauPwhBIpi5e5dO2RH4%2FPwb2m6unOPkGpIEhEXGKxeQdVQ%2FPyf3pgkriDkLWaAiuC8aEM%2BPPY%2FoPwjWokVWTdRbsHFb7Ac0lkCeeKfujpnWe3UqY9Y4df3r6zUS%2FMO3eyRHktt03bcDkjzB6JW4CYu3IqPcQouwWY26zSLNPBd4mBJnWis0nlWHmd9UCS0GcSlr5njbvUeb8Vsbf4rfLBtuCIyo3xOV%2FwIXI%2BeSEki9aY1AzT%2Ftg2KxxTk4lzURLzx9dmtGxy7cGOtkAl2%2FWashSXkhk3gOr%2FZb%2Fsyl0aJlCvc%2Bpjr%2Bt6m1dAqf6hPMa99odxdhfd%2FXx%2B1KInU3fNgWHz%2FgxKO7eSAwFiUB20JX6GG3I68MeR%2Ba9Qdy%2FCRFCRJEqt9KQ2VKwLpXbqbvtYRd7fej3F49CF134lEOlFZMlIuTlqynWbkpWMrYVV%2FOf%2F7hY%2BCWodB83qXDEkB9KqvmwvuAdpA5d%2Ft39aXOuW9q8MX9Rdwp1zhzU2tRXHV5VtvYGIBJpZN3jyfmi%2B5umPm8b4bVUaHXIvDZOrtKHolSYZq%2B3UynWbkpWMrYVV%2FOf%2F7hY%2BCUIgLGFBxlNIKFtymAwBSqOFU5yX5B36t6vtajXFxEn1cmr%2BCXkaIhXh5UVjLvhO%2B85ik%2FqNZkOmrcPhemPlYMsFsK0Emid4xeugGPF7C1%2BiN%2FhlbEl0fNfdld%2FnJIWr7KJYR%2FGV404hc2AwMdL1%2FB%2BHsoSTK3rjeyhOEDbAa1MgSvXSsfX7%2BscFWc%2BYvvoPvC7ayOEboA48eB99WQ0XUmP7R34sJgtSp0OS%2BJkPHfGpYmWndCfkyf7Utcu7aFB4Vw%3D%3D3sSs5e43c9311c7470cb4e6b030b71806f90e32cd227:48:8c0e2952-c947-11f0-a740-005056ae692b:0813c020e2; x-s3-tid=5e43c9311c7470cb4e6b030b71806f90e32cd227:48:8c0e2952-c947-11f0-a740-005056ae692b:0813c020e2; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
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

# response = requests.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', cookies=cookies, headers=headers, data=data)
print(response.status_code)