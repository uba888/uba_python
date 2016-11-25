#!/usr/bin/env python
import urllib.request
import re
import chardet
def getProxyIp():
    url='http://www.kuaidaili.com'
    response=urllib.request.urlopen(url).read()
    code=chardet.detect(response)['encoding']
    html=response.decode(code)
    re1=re.compile(r'data-title="IP">(.+?)</td>\n.+data-title="PORT">(.+?)<')
    ans=re.findall(re1,html)
    return ans
print(getProxyIp())
