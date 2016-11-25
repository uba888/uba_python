import requests
from scrapy import Selector

def geturl():
	url1='http://www.fenxs.com'
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	r1=requests.get(url1,headers=headers).text
	hxs1=Selector(text=r1)
	url2=hxs1.xpath('//*[@class="excerpt"]/div[1]/a/@href').extract()[1]
	return url2

def getzm(url):
	headers={'User-Agent': 'Mozilla/5.1 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	url2=url
	r2=requests.get(url2,headers=headers).text
	hxs2=Selector(text=r2)
	text=hxs2.xpath('//*[@class="article-content"]/p[7]/text()').extract()
	return text

if __name__=="__main__":
	url=geturl()
	text=getzm(url)
	for i in text:
		print(i)
	

 
