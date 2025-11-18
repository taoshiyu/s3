import requests

cookies = {
    'JSESSIONID': '425AF37FA60D0045318C144596297BAE',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219a8fd299671166-040d7f2c718d538-26061b51-2073600-19a8fd29968188f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219a8fd299671166-040d7f2c718d538-26061b51-2073600-19a8fd29968188f%22%7D',
    'x-s3-sid': 'S18jO3rksb91e344z4n7ojg2p',
    'arialoadData': 'false',
    'AlteonP': 'Acj5Om9ADgpYXDNpqZLcCA$$',
    'sw_rtk': 'Wf4z4n7ojgdj5VxlacAKe344cM23',
    'x-s3-s4e': 'dYA4ok%2BVAv0apopZQixNbzM73AisgazKhz8ZFf9liGCBJMqZyklGIzzFMBI9b0Lhceqqy0RWLLYAYglgEwcMMaTyy11vVwRVeiV1FtTvUqEn37rlgPhbOAb1psdWaGKFLlB5d73dN1CgjRDFcAoMOL1xzmLOPuchLPOTfK%2Bi63av3iqqKeCHyS7j8InYj4shFvpSiYSyZ63I4eztWO3W20Ci97qOa4xpmkta69j8VrDPpNi1BsYrAqzr4EvSPaKhruC7nDZ36POc%2FSPiG%2BkULtwfrQ5W61lvukYPcJmbGMVhHONXGomCL3Jk74BHPV7SOEYj%2BIVs%2B5%2FdzOBer3Ee4%2BT6chgtKlr9qSQeNXl3HGYaWuKvGJktks0mQpcaugUDundmFkE4P5ybHECNc9gIwqZIlbZCtEbsZ%2FjDyQFvF3Fg5VzdSQAnxB9z%2F45ye7xTB2JLIlBDH%2B9eUH7ZOBDMeudNhE5d4S6uDQY%2FIPixqanqrC%2BtCeEkT3aY%2F1%2FltGzXJLNfXWIMDpg%2BqSw7YBFTNpTnhMgLqE8mgIc4EZPqYZNg5VzdSQAnxB9z%2F45ye7xTBMVHF0PEVo9zWQLAX2SLhs%2Bcm47zxO1uSeUvMVULPAK%2FRhoBNPNVRtguj8vzylbBPUbY%2FoZnE4Ndc6AklszspZZapzHbxwqrtoqzco3R2oPqvHbSutMR1x7k6ccxJfPMLSTX59oZvuGSr7tF7lhp9CqQBgeHoK53jy%2BKcDWrEURewYiT8IyK0%2BCGVAVFnnRo%2BkCJqXsOs99UqVK7H4xIybuLxTS45X3faAXMPvayTXhRyeBpNN%2Bz5kh2hzAo8EpT3sSsbdbec2dfe035d78ed09097d73ac691ec55d08443:48:4a900515-c39e-11f0-a33d-3cd2e55daed6:6410012048',
    'x-s3-tid': 'bdbec2dfe035d78ed09097d73ac691ec55d08443:48:4a900515-c39e-11f0-a33d-3cd2e55daed6:6410012048',
    'fromPage': '%7BfromPage%3A%22index%22%7D',
    'sccode': '%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
    'ariauseGraymode': 'false',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.shenzhenair.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.shenzhenair.com/szair_B2C/flightsearch.action',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'JSESSIONID=425AF37FA60D0045318C144596297BAE; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219a8fd299671166-040d7f2c718d538-26061b51-2073600-19a8fd29968188f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219a8fd299671166-040d7f2c718d538-26061b51-2073600-19a8fd29968188f%22%7D; x-s3-sid=S18jO3rksb91e344z4n7ojg2p; arialoadData=false; AlteonP=Acj5Om9ADgpYXDNpqZLcCA$$; sw_rtk=Wf4z4n7ojgdj5VxlacAKe344cM23; x-s3-s4e=dYA4ok%2BVAv0apopZQixNbzM73AisgazKhz8ZFf9liGCBJMqZyklGIzzFMBI9b0Lhceqqy0RWLLYAYglgEwcMMaTyy11vVwRVeiV1FtTvUqEn37rlgPhbOAb1psdWaGKFLlB5d73dN1CgjRDFcAoMOL1xzmLOPuchLPOTfK%2Bi63av3iqqKeCHyS7j8InYj4shFvpSiYSyZ63I4eztWO3W20Ci97qOa4xpmkta69j8VrDPpNi1BsYrAqzr4EvSPaKhruC7nDZ36POc%2FSPiG%2BkULtwfrQ5W61lvukYPcJmbGMVhHONXGomCL3Jk74BHPV7SOEYj%2BIVs%2B5%2FdzOBer3Ee4%2BT6chgtKlr9qSQeNXl3HGYaWuKvGJktks0mQpcaugUDundmFkE4P5ybHECNc9gIwqZIlbZCtEbsZ%2FjDyQFvF3Fg5VzdSQAnxB9z%2F45ye7xTB2JLIlBDH%2B9eUH7ZOBDMeudNhE5d4S6uDQY%2FIPixqanqrC%2BtCeEkT3aY%2F1%2FltGzXJLNfXWIMDpg%2BqSw7YBFTNpTnhMgLqE8mgIc4EZPqYZNg5VzdSQAnxB9z%2F45ye7xTBMVHF0PEVo9zWQLAX2SLhs%2Bcm47zxO1uSeUvMVULPAK%2FRhoBNPNVRtguj8vzylbBPUbY%2FoZnE4Ndc6AklszspZZapzHbxwqrtoqzco3R2oPqvHbSutMR1x7k6ccxJfPMLSTX59oZvuGSr7tF7lhp9CqQBgeHoK53jy%2BKcDWrEURewYiT8IyK0%2BCGVAVFnnRo%2BkCJqXsOs99UqVK7H4xIybuLxTS45X3faAXMPvayTXhRyeBpNN%2Bz5kh2hzAo8EpT3sSsbdbec2dfe035d78ed09097d73ac691ec55d08443:48:4a900515-c39e-11f0-a33d-3cd2e55daed6:6410012048; x-s3-tid=bdbec2dfe035d78ed09097d73ac691ec55d08443:48:4a900515-c39e-11f0-a33d-3cd2e55daed6:6410012048; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D; ariauseGraymode=false',
}

data = {
    'condition.orgCityCode': 'SZX',
    'condition.dstCityCode': 'HFE',
    'condition.hcType': 'DC',
    'condition.orgDate': '2025-11-17',
    'condition.dstDate': '2025-11-17',
}

response = requests.post('https://www.shenzhenair.com/szair_B2C/flightSearch.action', cookies=cookies, headers=headers, data=data)
print(response.text)