import os
import requests

cookies = {
    'JSESSIONID': '20857963996EF44A33F886F9921FCADB',
    'AlteonP': 'BZhwDW9ADgrYb6U7/VwkPQ' + os.getenv('$', ''),
    'HMF_CI': '3b738fea8b4ce36af9597f0b18513e204fc196291a3f0a39c07710dd95bc94658333d9ff0bd6ed8b9b8a2d306561f39ad0cf3087fdbc47c71b312b9c041ea07f14',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219ab23993490-0d9b7ee6e2d26a-26061b51-2073600-19ab239934a155c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab23993490-0d9b7ee6e2d26a-26061b51-2073600-19ab239934a155c%22%7D',
    'arialoadData': 'false',
    'x-s3-sid': 'S1dq1gibsmSIe34413lm9ba38',
    'ariauseGraymode': 'false',
    'x-s3-s4e': '%2FNVDZy0Cx6pVW0zDDFE2T%2BW5ZYHAwoS%2BVl4JgiEXZG2p0QMGG31EgI227MiUbYSjS1AUm4RptOfIRIdqcTbZqvIpmYB9QhErrcr8sd%2FrVitO2WIxwpn03RzwRP2B8JtUB6bvVRqqxMXrmM0xvWSWVyjGGF7bf9Sc3qPaZoqTqFo1pNXt2DPuEprEMKCOrQwzPPh7XvGG9rTIvuv63JqiaHM6dTjSlv%2FTq%2BEZYcUm%2FdeH4UQPQYMUY7epbxLy33OIBDWtqcYJOON%2B7IzVCIiu9vEXpX%2F78CfcTfQrblU68q4ea4WN%2FhooDPTFfCjdzOtrniBwXKKwZv9TVJIs7GMFQHgYCKtdkcwyfxYmt1SrEWBJ7XrCWxXsQvgWPML5rmCT6yfdHDcFj5viPE88a9DTdg7HqBiXIy0Tp59tIQKPLTPTs%2BDst%2FV9vTs9YPdn%2Bx%2FME0Wxy%2F8ot91aAvsmygROhPcirWCsF3HVHKsbOTVW%2FnuekZwVi7atImttoOLadDHlIr41UMztySit%2FuSFsft%2B9vfG25uwpFBVDLmInfcR6FArs2jc8BxeVLvghGG9HBD4E0Wxy%2F8ot91aAvsmygROhGkRWtkCfDUsarFJ7Wq7vqNxqBA0d6EHby4NYfk8PaYmIXGnFXrxeU%2FvriM77R9ObFIEYLuzZpxMxqT4%2BzKed7AprR%2B%2Bu6T58tcESYpv17VxSeF36gOY9qG2F4QFtF1DXNqMRpi2H8VfqN8Kd4Lty6gCrrzrrBsB0QWyQ0E3Xu%2BYwWSyif87TZpvJe4QUFdzc425ZqFuDMOGoirqFiG31vq8u0iWQmMwklyKVwZmwck06yn5Q14GgDB3TbuR%2FX%2FqhQ%3D%3D3sSs1ef59452806deee43d64a84021216d6120b3f98a:48:7fc7cbb8-c8a4-11f0-a740-005056ae692b:0c2080201e',
    'x-s3-tid': '1ef59452806deee43d64a84021216d6120b3f98a:48:7fc7cbb8-c8a4-11f0-a740-005056ae692b:0c2080201e',
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
    # 'Cookie': 'JSESSIONID=20857963996EF44A33F886F9921FCADB; AlteonP=BZhwDW9ADgrYb6U7/VwkPQ' + os.getenv('$', '') + '; HMF_CI=3b738fea8b4ce36af9597f0b18513e204fc196291a3f0a39c07710dd95bc94658333d9ff0bd6ed8b9b8a2d306561f39ad0cf3087fdbc47c71b312b9c041ea07f14; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219ab23993490-0d9b7ee6e2d26a-26061b51-2073600-19ab239934a155c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ab23993490-0d9b7ee6e2d26a-26061b51-2073600-19ab239934a155c%22%7D; arialoadData=false; x-s3-sid=S1dq1gibsmSIe34413lm9ba38; ariauseGraymode=false; x-s3-s4e=%2FNVDZy0Cx6pVW0zDDFE2T%2BW5ZYHAwoS%2BVl4JgiEXZG2p0QMGG31EgI227MiUbYSjS1AUm4RptOfIRIdqcTbZqvIpmYB9QhErrcr8sd%2FrVitO2WIxwpn03RzwRP2B8JtUB6bvVRqqxMXrmM0xvWSWVyjGGF7bf9Sc3qPaZoqTqFo1pNXt2DPuEprEMKCOrQwzPPh7XvGG9rTIvuv63JqiaHM6dTjSlv%2FTq%2BEZYcUm%2FdeH4UQPQYMUY7epbxLy33OIBDWtqcYJOON%2B7IzVCIiu9vEXpX%2F78CfcTfQrblU68q4ea4WN%2FhooDPTFfCjdzOtrniBwXKKwZv9TVJIs7GMFQHgYCKtdkcwyfxYmt1SrEWBJ7XrCWxXsQvgWPML5rmCT6yfdHDcFj5viPE88a9DTdg7HqBiXIy0Tp59tIQKPLTPTs%2BDst%2FV9vTs9YPdn%2Bx%2FME0Wxy%2F8ot91aAvsmygROhPcirWCsF3HVHKsbOTVW%2FnuekZwVi7atImttoOLadDHlIr41UMztySit%2FuSFsft%2B9vfG25uwpFBVDLmInfcR6FArs2jc8BxeVLvghGG9HBD4E0Wxy%2F8ot91aAvsmygROhGkRWtkCfDUsarFJ7Wq7vqNxqBA0d6EHby4NYfk8PaYmIXGnFXrxeU%2FvriM77R9ObFIEYLuzZpxMxqT4%2BzKed7AprR%2B%2Bu6T58tcESYpv17VxSeF36gOY9qG2F4QFtF1DXNqMRpi2H8VfqN8Kd4Lty6gCrrzrrBsB0QWyQ0E3Xu%2BYwWSyif87TZpvJe4QUFdzc425ZqFuDMOGoirqFiG31vq8u0iWQmMwklyKVwZmwck06yn5Q14GgDB3TbuR%2FX%2FqhQ%3D%3D3sSs1ef59452806deee43d64a84021216d6120b3f98a:48:7fc7cbb8-c8a4-11f0-a740-005056ae692b:0c2080201e; x-s3-tid=1ef59452806deee43d64a84021216d6120b3f98a:48:7fc7cbb8-c8a4-11f0-a740-005056ae692b:0c2080201e; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
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