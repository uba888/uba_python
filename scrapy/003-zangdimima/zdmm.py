#!/usr/bin/python3

import requests
import chardet
import os
import random
from scrapy import Selector



def get_zhang(url):
	requests.adapters.DEFAULT_RETRIES=5
	response_zhang=requests.get(url,headers=get_headers())
	code=chardet.detect(response_zhang.content)['encoding']
	if code=='GB2312':
		response_zhang.encoding='GBK'
	else:
		response_zhang.encoding=code
	xp_zhang=Selector(text=response_zhang.text)
	zhang_content=xp_zhang.xpath('//body/div[@class="container"]/h3/text()').extract()
	curpath=os.getcwd()

	
	os.mkdir('藏地密码')
	root_dir=os.path.join(curpath,'藏地密码')
	os.chdir('藏地密码')
	for i in range(len(zhang_content)):
		os.mkdir(zhang_content[i])
		os.chdir(zhang_content[i])
		if i==0:
			content1=xp_zhang.xpath('//body/div[@class="container"]/p/text()').extract()
			print(zhang_content[i])
			with open(zhang_content[i],'w+') as cp1:
				for i in content1:
					cp1.writelines(i+'\n')
		else:
			mulu=xp_zhang.xpath("//body/div[@class=\"container\"]/div[%s]/ul/li/a/@title" % i).extract()
			mulu_site=xp_zhang.xpath("//body/div[@class=\"container\"]/div[%s]/ul/li/a/@href" % i).extract()
			for j in range(len(mulu)):
#				time.sleep(2)
				content=get_content(mulu_site[j])
				print(mulu[j])
				with open(mulu[j],'w+') as cp2:
					for i in content:
						cp2.writelines(i+'\n')
		os.chdir(root_dir)
	return zhang_content


def get_content(url):
	while True:
		try:	
			response_content=requests.get(url,headers=get_headers())
			code=chardet.detect(response_content.content)['encoding']
			if code=='GB2312':
				response_content.encoding='GBK'
			else:
				response_content.encoding=code
			xp_content=Selector(text=response_content.text)
			content=xp_content.xpath('//body/div[@class="container"]//div[@class="span9"]/p/text()').extract()
			return content
				
		except:
			pass

def get_headers():
	headers_model=['User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0','User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko','User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0','User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)','User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11','User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11','User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11','User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)','User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)','User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
	headers={}
	headers['User-Agent']=headers_model[random.randint(0,13)]
	return headers

if __name__=="__main__":
	if os.path.exists('藏地密码'):
		judge=input("藏地密码目录已存在,请先删除，确认删除请按Y:")
		if judge=='Y':
			os.system('rm -rf 藏地密码')
			main_url='http://www.zangdimima8.com/'
			get_zhang(main_url)
		else:
			print("请先处理该目录")
		
	else:
		main_url='http://www.zangdimima8.com/'
		get_zhang(main_url)	
