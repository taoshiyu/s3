import os
import requests

cookies = {
    'JSESSIONID': '332E7189F4A557F1DF641B65715FE376',
    'AlteonP': 'BdX4IG9ADgo3m5UjhgokNQ$$' ,
    'HMF_CI': '5730f48bdc2511b163627ff792eaafdacdf2df9bca48f241c5c7d84ff31fe863a96d5be106faad398e06525d360cba84bf1d0ec49647955e5bd5488ccae2e65ce4',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219abaa58df036c-0e615822877ad1-26061b51-2073600-19abaa58df11269%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219abaa58df036c-0e615822877ad1-26061b51-2073600-19abaa58df11269%22%7D',
    'x-s3-sid': 'S1rsLC2dhpC5e344z4nal7q2j',
    'ariauseGraymode': 'false',
    'arialoadData': 'false',
    'x-s3-s4e': '8%2B%2BSZ8IL0aNAzaiGdsP%2FN5Ooly8Q%2BEFvUEeX%2F6Kk1kXemJdRmV9JbU9WTV9T2L4b2KCSJGRi2pwEvSdxhocIdY4AEkhrUvlR2DGg2X47D1CKj3dcDFWDibHkx7Ok4G0P7Ak%2FoBTPIOGHHD%2BFkyUWGGyjEGLqlpXuNrr6owbfJK1%2B5gegiByi4yajTfQeWUoSpLtiBy0RPKZHCpxjc4IWhmvYZeXrK%2FGERG353FL6r3yrdTWS8Er3%2BN80A153rwb3JH27c9mDHhbGBftiBvYGBT18noD845zHwopFD7W91dzej3oauuAud4yTGxQY1LnEby0Hij%2FuL9w5n6SbotP0oObwE4qluhiJhOA8AOYSZ0%2BkaZ1qPWo%2FB6EMdal%2FZlVD394AQ3IAHscPvUy%2B3BYW1DjBaVvji1%2F6ivDn3Ks59dgUjp2KTo59crw%2BKf%2B5s9qFbbyNuCtPdTkHkzv1zt9sdtotTV0nB82crLJiyxpHCYcKUWYd6hYV3Ep8BBhIOTEVQEApaVvTnATTvW%2FT9sHfO9BV%2Fhoyvf2XBkWX7W%2BiZ1dZ%2FEI4T3RbfhgGMSKt8xwabbyNuCtPdTkHkzv1zt9sdp9cXhSb%2Bdt5Dl84CiVHx82IWfAuve%2B0exq%2B6q%2FzI65yVj4ydjibImNDNAXnkPmOahhXcxh2mElEtuBJF22ZBMeDfwR%2BEUzKoIxx6P6dGyRKMW6h2Tvatt8IINDri0gO203dK7Zw9J1tny86B17Rx93nJAFiD%2FL42KFkNvZ841XR5ATKjfYJC9m2gstov4xvK7IeF9rbGMuvEBJhfSLFW2XFj6kuLyM4KU30J%2FoMTJeAfPDehNYh7Kuwq5QjgH9Avg%3D%3D3sSs00b1969588274b1d3a85934d345fcb08ba3552ea:48:f6f3e784-c9ec-11f0-a33d-3cd2e55daed6:0400f320f9',
    'x-s3-tid': '00b1969588274b1d3a85934d345fcb08ba3552ea:48:f6f3e784-c9ec-11f0-a33d-3cd2e55daed6:0400f320f9',
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
    # 'Cookie': 'JSESSIONID=332E7189F4A557F1DF641B65715FE376; AlteonP=BdX4IG9ADgo3m5UjhgokNQ' + os.getenv('$', '') + '; HMF_CI=5730f48bdc2511b163627ff792eaafdacdf2df9bca48f241c5c7d84ff31fe863a96d5be106faad398e06525d360cba84bf1d0ec49647955e5bd5488ccae2e65ce4; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219abaa58df036c-0e615822877ad1-26061b51-2073600-19abaa58df11269%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219abaa58df036c-0e615822877ad1-26061b51-2073600-19abaa58df11269%22%7D; x-s3-sid=S1rsLC2dhpC5e344z4nal7q2j; ariauseGraymode=false; arialoadData=false; x-s3-s4e=8%2B%2BSZ8IL0aNAzaiGdsP%2FN5Ooly8Q%2BEFvUEeX%2F6Kk1kXemJdRmV9JbU9WTV9T2L4b2KCSJGRi2pwEvSdxhocIdY4AEkhrUvlR2DGg2X47D1CKj3dcDFWDibHkx7Ok4G0P7Ak%2FoBTPIOGHHD%2BFkyUWGGyjEGLqlpXuNrr6owbfJK1%2B5gegiByi4yajTfQeWUoSpLtiBy0RPKZHCpxjc4IWhmvYZeXrK%2FGERG353FL6r3yrdTWS8Er3%2BN80A153rwb3JH27c9mDHhbGBftiBvYGBT18noD845zHwopFD7W91dzej3oauuAud4yTGxQY1LnEby0Hij%2FuL9w5n6SbotP0oObwE4qluhiJhOA8AOYSZ0%2BkaZ1qPWo%2FB6EMdal%2FZlVD394AQ3IAHscPvUy%2B3BYW1DjBaVvji1%2F6ivDn3Ks59dgUjp2KTo59crw%2BKf%2B5s9qFbbyNuCtPdTkHkzv1zt9sdtotTV0nB82crLJiyxpHCYcKUWYd6hYV3Ep8BBhIOTEVQEApaVvTnATTvW%2FT9sHfO9BV%2Fhoyvf2XBkWX7W%2BiZ1dZ%2FEI4T3RbfhgGMSKt8xwabbyNuCtPdTkHkzv1zt9sdp9cXhSb%2Bdt5Dl84CiVHx82IWfAuve%2B0exq%2B6q%2FzI65yVj4ydjibImNDNAXnkPmOahhXcxh2mElEtuBJF22ZBMeDfwR%2BEUzKoIxx6P6dGyRKMW6h2Tvatt8IINDri0gO203dK7Zw9J1tny86B17Rx93nJAFiD%2FL42KFkNvZ841XR5ATKjfYJC9m2gstov4xvK7IeF9rbGMuvEBJhfSLFW2XFj6kuLyM4KU30J%2FoMTJeAfPDehNYh7Kuwq5QjgH9Avg%3D%3D3sSs00b1969588274b1d3a85934d345fcb08ba3552ea:48:f6f3e784-c9ec-11f0-a33d-3cd2e55daed6:0400f320f9; x-s3-tid=00b1969588274b1d3a85934d345fcb08ba3552ea:48:f6f3e784-c9ec-11f0-a33d-3cd2e55daed6:0400f320f9; fromPage=%7BfromPage%3A%22index%22%7D; sccode=%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
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
print(response.status_code, response.cookies.get_dict())