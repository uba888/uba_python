#!/usr/bin/python3

import requests,os
from scrapy import Selector

#cur_dir='/alidata/uba_python/scrapy/005-seafile/test'
cur_dir='/var/www/piwik/uba'
r1=requests.get("https://manual-cn.seafile.com")
r1.encoding="utf8"
print(r1)
sea=Selector(text=r1.text)
for i in range(1,15):
	title=sea.xpath('//ul[@class="summary"]/li[%d]/a/text()' % i).extract()
	for j in range(len(title)):
		print(title[j].strip())
		os.chdir(cur_dir)
		os.mkdir(title[j].strip())
	sb=sea.xpath('//ul[@class="summary"]/li[%d]/ul/li/a/text()' % i).extract()
	sb_href=sea.xpath('//ul[@class="summary"]/li[%d]/ul/li/a/@href' % i).extract()
	for x in range(len(sb)):
		print("\t"+sb[x].strip()+"【https://manual-cn.seafile.com/"+sb_href[x].strip()+"】")
		os.chdir(os.path.join(cur_dir,title[j].strip()))
		r2=requests.get("https://manual-cn.seafile.com/"+sb_href[x].strip())
		r2.encoding="utf8"
		try:
			with open(sb[x].strip()+".html",'w+') as x:
				x.writelines(r2.text+'\n')
		except:
			pass
			
