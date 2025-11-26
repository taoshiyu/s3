import os
import requests

cookies = {
    'JSESSIONID': '97DF6F0FAAF9B31645D7F9082A3C9DB1',
    'AlteonP': 'AWFsOG9ADgqpnNEHNjdSKA$$',
    'HMF_CI': '43577111c53d46f317cfe295fc901ff7bbc356098cb9595941b328e4b8f93165ef12e88892b923f61c1adc8343bdf122a2425c56312f647389d789931c49b79ede',
    'ariauseGraymode': 'false',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219ac115701e0-0165b54d970da78-26061b51-2073600-19ac115701f16da%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219ac115701e0-0165b54d970da78-26061b51-2073600-19ac115701f16da%22%7D',
    'arialoadData': 'false',
    'x-s3-sid': 'S15qCv6cjrT9e34413lm9ba33',
    'x-s3-s4e': 'rCl6Jbbz9OOpXp0qequyqYPuZd1egvAvn8OI3xfnE%2B0N4PKxaRvg6ZtaO%2BO1fwLa49Qyz%2F7GHTF%2F%2BlDSGwGOOaLbMDc1sIO9vBUY0EhShxwqEOsunGMdhLUfaRBTl4mvAq9%2FmaVorcHGZo4JsiXCjpEBjiVXb1T8zp8s6jQS0ZNxa8kaH6HITeoaHBtq1ZS62ojqzUtyeLUti0rqsHXCrQd1L8SXuu%2FauoE%2FYRNurOqStvjc4Rn80EqJY0CEAnztvIcipoy1U5KHUUmKXHsgIt92dksOeMNGbYhanfhCtEgD%2BrLZ%2F0jwlVJRV750UGJjSeAQ0PcvnXNBglfc2Fgi5hAnu%2BWePz7yTkD1ftbwOsqo6ispXP6R9WlWU7VpwHl8vxQ5kk53wjqY6GSHTGnBIYCsr2OPd4ptbGEtkBE2NIzhqlZLFBrp1idwRxhcm1I9cFxRhrpvU2wT5rmmeQN6L36jjgMVYdBrFG%2F%2FXVBVW%2FQqcQFXlvJLynMnptgX%2B1y7pzWYJV2f9VD3sjmaAafXWVCl7RW0u3y%2FT06oW%2FuVRwZbt1to7iN2uEHr9TzP9m6BcFxRhrpvU2wT5rmmeQN6LyxtnmaCLZ2tCKyfBYIGdTLdO%2BS%2Bc4uWqIx901qx0s6SwS8rAgY6MRGt%2BDSlmYToX2n7X3pMy%2FgMrpY9tqIoDHRF3NaXHmuDYxZLSbMZTyHqvgljT9oYK2MeH8KFZ7uG1vlrU5L7i5IiRqWtDkENP8sETMcBhJ6kjo3YJ%2BJ7Co2LGprMUelqqOw7QweL8HNS58hZMG64AxvvJeep2bJzRK1uF2AmpWXbYkIqVbY5g7zXHiVqUZxq9JsrXC%2BsAmwduA%3D%3D3sSs2cffc88fac96a6ee5b70f1e885951dfed24b5f9d:48:7019f913-cae8-11f0-a740-005056ae692b:8020c12089',
    'x-s3-tid': '2cffc88fac96a6ee5b70f1e885951dfed24b5f9d:48:7019f913-cae8-11f0-a740-005056ae692b:8020c12089',
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
    'orgDate': '2025-11-27',
    'dstDate': '2025-11-27',
    'quiz': [
        'Y',
        '1',
    ],
    'bzcPsgrName': '',
    'bzcCertNo': '',
}

response = requests.post('https://www.shenzhenair.com/szair_B2C/flightsearch.action', cookies=cookies, headers=headers, data=data)
print(response.text)