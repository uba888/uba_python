import requests
import sys
import socket
ip=socket.getaddrinfo(sys.argv[1],'http')[0][4][0]
url='http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip
r1=requests.get(url)
print(r1.json()['data']['isp'])
