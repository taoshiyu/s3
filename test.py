
import requests
r=requests.post(url='http://ip.taobao.com/service/getIpInfo2.php', data={'ip': 'myip'},verify=False)
print(r.status_code)
print(r.json())
