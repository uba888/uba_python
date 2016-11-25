import requests
from scrapy import Selector

url='http://bbs.fishc.com'
def get_url():
	sum=0
	for i in range(1,6):
		z_url=url+'/forum-243-'+str(i)+'.html'
		sum=get_text(z_url,sum)
		
def get_text(z_url,sum):
	text=requests.get(z_url).text
	hxs=Selector(text=text)
	title=hxs.xpath('//th/a[2]/text()').extract()
	add=hxs.xpath('//th/a[2]/@href').extract()
#	author=hxs.xpath('//td[@class="by"]/cite/a[@style="color: #00FF7F;"]/font/text()').extract()
#	leixing=hxs.xpath('//th/em/a/text()').extract()
	for x in range(len(title)):
		sum+=1
		print(str(sum)+"##"+title[x]+"======>"+url+"/"+add[x])
	return sum
get_url()
