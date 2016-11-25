#!/usr/bin/env python
#encoding=utf-8
import chardet
import urllib.request
def get_unicode(url):
	content=urllib.request.urlopen(url).read()
	decode=chardet.detect(content)
	ans=decode['encoding']
	return ans
urllist=['http://www.jd.com','http://www.baidu.com','http://www.clickplus.cn','http://www.163.com']
for i in urllist:
	a=get_unicode(i)
	print(i,a)
	


