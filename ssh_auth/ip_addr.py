#!/usr/bin/python3
import socket
import requests
import sys
ip=sys.argv[1]
response=requests.get('http://api.ip138.com/query/?ip=%s&datatype=jsonp&token=4d977467f918b9c90b242ce0fc20b069' % ip)
result=response.json()['data']

print(result)
