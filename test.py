import os
import requests



cookies = {
    'JSESSIONID': '7632AA209747D8451EE40DFB6510BA49',
    'HMF_CI': '352b099c85206b939c480c266ce96eb4b2b2348ae37740c92b92bd0302cc6339c2696a104641b80ba7fbaa2ab17ed6257128b6b170c04f64c3ab33254dce5970b5',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219ab2387595b18-080b0c784f9dd5-26061b51-2073600-19ab238759613ec%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab2387595b18-080b0c784f9dd5-26061b51-2073600-19ab238759613ec%22%7D',
    'x-s3-sid': 'S14r2ag6smePe34413lm9ba2c',
    'arialoadData': 'false',
    'sw_rtk': 'WHS13lm9ba8ndp99ppMRe344kV3a',
    'AlteonP': 'AjZHKG9ADgp+FGVl5EVuGA$$' ,
    'ariauseGraymode': 'false',
    'x-s3-s4e': '67iwZzAC1iKtMI7FLI1%2Biv%2FG7TINg92Vm30oqge3G%2Bekwo%2FK8b%2BVnTA%2FTmruxAAd95LYl71d9UOrnbvxq3R%2FBpuo7W5AtgqDxT5A2aD3d54LWL%2Bl1ptvnbwMW%2Fw8%2BVTBS41zh6JjwGDECd39Z4jVxWXlFLZ1IjP8HLRdy8Rfz6YpL%2FZjY4N11BiZA90Rjz4PYO2A0%2BI9b3auldsi1mEzM45AkTHK0JUR5UW0Y9sE4q3MXUitj54v8lg%2B8l5YjHhFTR9DfUUY41O9k355OH3y%2F15QdiOjTcb9KAXdV%2F6Pmiaa4fJ%2BPIgm8uKKXYUblwsG02ffDVIMGGmrDLInOECoghhKVXdLV6hTjqB33jIht%2BtTaERCAyXWIjzVHI9kZqQCfU1Ubxz6pJEOe1g%2F25Yyg8Q%2F%2FNr5pQThFE4BOwRVK7GG8ZDs7DsRNGg9EL%2FMJBghrqofZ0%2BXI7T19eWcmtqBF5unpSb2RIkuyDBXzdOI3LWGYjcT%2F5LkTX8ZJiQ3FpyK1GIXGhqUqkSnr6UfO8w8fCuWIeHBOkfWEZcllDYeeBWluQGWReraOOpfvz0g89MIrqofZ0%2BXI7T19eWcmtqBFykWj3m3gduydeC7ogBYlNHMWxo2tIYX7%2FUrqxWg5ISBbe9n%2BPRKm0tGqqZb33Ik42NLfmPRMKZbJp2MpvikM6TugBZXOTFW%2Bmk11iCrnu5ThbjXVCP%2FE7MzJnf0xubNML5GIx3EU%2BI%2FEH%2BfCJkhqUhxesHoPPVH84gbt5RdQS5QOxXfU%2BPpuFDyUxBTx%2FKxZBvT1CCpA9l0dZfuz%2Fob5%2FEK%2Bz%2B6C7mGT4SMSqtOC3WbMWulKI%2FmoOa30aKDmBCnoQ%3D%3D3sSs007e19795f28bacae945fd0f61053a8d96ca6c77:48:2464db9e-ca08-11f0-a33d-3cd2e55daed6:0010c320cd',
    'x-s3-tid': '007e19795f28bacae945fd0f61053a8d96ca6c77:48:2464db9e-ca08-11f0-a33d-3cd2e55daed6:0010c320cd',
    'fromPage': '%7BfromPage%3A%22index%22%7D',
    'sccode': '%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
}
cookies.update(
    {
    'x-s3-sid': 'S14r2ag6smePe34413lm9ba2c',
    'x-s3-s4e': '67iwZzAC1iKtMI7FLI1%2Biv%2FG7TINg92Vm30oqge3G%2Bekwo%2FK8b%2BVnTA%2FTmruxAAd95LYl71d9UOrnbvxq3R%2FBpuo7W5AtgqDxT5A2aD3d54LWL%2Bl1ptvnbwMW%2Fw8%2BVTBS41zh6JjwGDECd39Z4jVxWXlFLZ1IjP8HLRdy8Rfz6YpL%2FZjY4N11BiZA90Rjz4PYO2A0%2BI9b3auldsi1mEzM45AkTHK0JUR5UW0Y9sE4q3MXUitj54v8lg%2B8l5YjHhFTR9DfUUY41O9k355OH3y%2F15QdiOjTcb9KAXdV%2F6Pmiaa4fJ%2BPIgm8uKKXYUblwsG02ffDVIMGGmrDLInOECoghhKVXdLV6hTjqB33jIht%2BtTaERCAyXWIjzVHI9kZqQCfU1Ubxz6pJEOe1g%2F25Yyg8Q%2F%2FNr5pQThFE4BOwRVK7GG8ZDs7DsRNGg9EL%2FMJBghrqofZ0%2BXI7T19eWcmtqBF5unpSb2RIkuyDBXzdOI3LWGYjcT%2F5LkTX8ZJiQ3FpyK1GIXGhqUqkSnr6UfO8w8fCuWIeHBOkfWEZcllDYeeBWluQGWReraOOpfvz0g89MIrqofZ0%2BXI7T19eWcmtqBFykWj3m3gduydeC7ogBYlNHMWxo2tIYX7%2FUrqxWg5ISBbe9n%2BPRKm0tGqqZb33Ik42NLfmPRMKZbJp2MpvikM6TugBZXOTFW%2Bmk11iCrnu5ThbjXVCP%2FE7MzJnf0xubNML5GIx3EU%2BI%2FEH%2BfCJkhqUhxesHoPPVH84gbt5RdQS5QOxXfU%2BPpuFDyUxBTx%2FKxZBvT1CCpA9l0dZfuz%2Fob5%2FEK%2Bz%2B6C7mGT4SMSqtOC3WbMWulKI%2FmoOa30aKDmBCnoQ%3D%3D3sSs007e19795f28bacae945fd0f61053a8d96ca6c77:48:2464db9e-ca08-11f0-a33d-3cd2e55daed6:0010c320cd',
    'x-s3-tid': '007e19795f28bacae945fd0f61053a8d96ca6c77:48:2464db9e-ca08-11f0-a33d-3cd2e55daed6:0010c320cd',
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
    # 'Cookie': 'JSESSIONID=7632AA209747D8451EE40DFB6510BA49; HMF_CI=352b099c85206b939c480c266ce96eb4b2b2348ae37740c92b92bd0302cc6339c2696a104641b80ba7fbaa2ab17ed6257128b6b170c04f64c3ab33254dce5970b5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ab2387595b18-080b0c784f9dd5-26061b51-2073600-19ab238759613ec%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab2387595b18-080b0c784f9dd5-26061b51-2073600-19ab238759613ec%22%7D; x-s3-sid=S14r2ag6smePe34413lm9ba2c; arialoadData=false; sw_rtk=WHS13lm9ba8ndp99ppMRe344kV3a; AlteonP=AjZHKG9ADgp+FGVl5EVuGA' + os.getenv('$', '') + '; ariauseGraymode=false; x-s3-s4e=67iwZzAC1iKtMI7FLI1%2Biv%2FG7TINg92Vm30oqge3G%2Bekwo%2FK8b%2BVnTA%2FTmruxAAd95LYl71d9UOrnbvxq3R%2FBpuo7W5AtgqDxT5A2aD3d54LWL%2Bl1ptvnbwMW%2Fw8%2BVTBS41zh6JjwGDECd39Z4jVxWXlFLZ1IjP8HLRdy8Rfz6YpL%2FZjY4N11BiZA90Rjz4PYO2A0%2BI9b3auldsi1mEzM45AkTHK0JUR5UW0Y9sE4q3MXUitj54v8lg%2B8l5YjHhFTR9DfUUY41O9k355OH3y%2F15QdiOjTcb9KAXdV%2F6Pmiaa4fJ%2BPIgm8uKKXYUblwsG02ffDVIMGGmrDLInOECoghhKVXdLV6hTjqB33jIht%2BtTaERCAyXWIjzVHI9kZqQCfU1Ubxz6pJEOe1g%2F25Yyg8Q%2F%2FNr5pQThFE4BOwRVK7GG8ZDs7DsRNGg9EL%2FMJBghrqofZ0%2BXI7T19eWcmtqBF5unpSb2RIkuyDBXzdOI3LWGYjcT%2F5LkTX8ZJiQ3FpyK1GIXGhqUqkSnr6UfO8w8fCuWIeHBOkfWEZcllDYeeBWluQGWReraOOpfvz0g89MIrqofZ0%2BXI7T19eWcmtqBFykWj3m3gduydeC7ogBYlNHMWxo2tIYX7%2FUrqxWg5ISBbe9n%2BPRKm0tGqqZb33Ik42NLfmPRMKZbJp2MpvikM6TugBZXOTFW%2Bmk11iCrnu5ThbjXVCP%2FE7MzJnf0xubNML5GIx3EU%2BI%2FEH%2BfCJkhqUhxesHoPPVH84gbt5RdQS5QOxXfU%2BPpuFDyUxBTx%2FKxZBvT1CCpA9l0dZfuz%2Fob5%2FEK%2Bz%2B6C7mGT4SMSqtOC3WbMWulKI%2FmoOa30aKDmBCnoQ%3D%3D3sSs007e19795f28bacae945fd0f61053a8d96ca6c77:48:2464db9e-ca08-11f0-a33d-3cd2e55daed6:0010c320cd; x-s3-tid=007e19795f28bacae945fd0f61053a8d96ca6c77:48:2464db9e-ca08-11f0-a33d-3cd2e55daed6:0010c320cd; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
    'Content-Type': 'application/x-www-form-urlencoded',
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

response = requests.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', cookies=cookies, headers=headers, data=data)