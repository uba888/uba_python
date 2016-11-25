import requests
from scrapy import Selector

def get_hxs(url):
	text=requests.get(url).text
	hxs=Selector(text=text)
	return hxs

def get_parent(hxs):
	url="http://bbs.fishc.com/"
	parent_title=hxs.xpath('//div[@class="fl_icn_g"]/a/img/@alt').extract()
	parent_url=hxs.xpath('//div[@class="fl_icn_g"]/a/@href').extract()
	for i in range(len(parent_url)):
		print(str(i)+"##"+parent_title[i])
	while True:
		content=input('你输入要查询的目录序号：')
		if int(content) in range(len(parent_url)):
			f_url=url+parent_url[int(content)]
			get_son(f_url)
		else:
			print('print error')
#	get_son(f_url)		


def get_son(url):
	hxs=get_hxs(url)
	son_title=hxs.xpath('//td[@class="fl_icn"]/a/img/@alt').extract()
	son_url=hxs.xpath('//td[@class="fl_icn"]/a/@href').extract()
	if len(son_url)==0:
		print("no content")
	else:
		for i in range(len(son_url)):
			print(son_title[i]+"\t"+"http://bbs.fishc.com/"+son_url[i])

if __name__=="__main__":
	url='http://bbs.fishc.com'
	hxs=get_hxs(url)
	get_parent(hxs)




	
