#!/usr/bin/python3

import requests
import pymongo
import sys
import time
from scrapy import Selector

def mongodb_connect():
	clt=pymongo.MongoClient('192.168.31.131',27017)
	clt.admin.authenticate('uba','q')
	return clt.douban.movie


def get_content(url):
	response=requests.get(url)
	xp=Selector(text=response.text)
	num=xp.xpath('//ol[@class="grid_view"]/li//div[@class="pic"]/em/text()').extract()
	title=xp.xpath('//ol[@class="grid_view"]/li//div[@class="info"]//span[1][@class="title"]/text()').extract()
	href=xp.xpath('//ol[@class="grid_view"]/li//div[@class="info"]/div/a/@href').extract()
	ps=xp.xpath('//ol[@class="grid_view"]/li//div[@class="info"]/div[@class="bd"]/p[1]').xpath('string(.)').extract()
	score=xp.xpath('//ol[@class="grid_view"]/li//div[@class="info"]//span[@class="rating_num"]/text()').extract()
	print(num)
	if len(href)==len(title)==len(ps)==len(score):
		for i in range(0,len(title)):
			#print("#####"+num[i]+"######")
			#print(title[i],href[i],"\n",ps[i].strip().replace('\n','').replace(' ',''),"\n",score[i])
			data={}
			data2={}
			data['title']=title[i]
			data['score']=score[i]	
			data['main_url']=href[i]
			data['ps']=ps[i].strip().replace('\n','').replace(' ','')
			data['see_addr'],data['price']=get_addr(href[i])		
			data2=data.copy()
			data2['_id']=num[i]
			try:
				cll.insert_one(data2)
			except: 
				cll.update_one({'_id':num[i]},{'$set':data})
			sys.stdout.write('进度:{0}%,时间:{1}s\r'.format((int(num[i])+1)*100/250,int(time.time()-begin)))
			sys.stdout.flush()
	else:
		print("scrapy error,pagenum !=")
	try: 
		next_page=xp.xpath('//span[@class="next"]/a/@href').extract()[0]
		get_content(main_url+next_page)
	except:
		print("scrapy end!")

def get_addr(url):
	response=requests.get(url)
	xp2=Selector(text=response.text)
	addr=xp2.xpath('//ul[@class="bs"]/li/a/text()').extract()
	site=xp2.xpath('//ul[@class="bs"]/li/a/@href').extract()
	price=xp2.xpath('//ul[@class="bs"]/li/span/span/text()').extract()
	allsite={}
	prices='charge'
	if len(addr)==len(site)==len(price)!=0:
		for i in range(0,len(addr)):
			#print(addr[i].strip().replace('\n','').replace(' ',''),site[i].strip().replace('\n','').replace(' ',''),price[i].strip().replace('\n','').replace(' ',''))
			allsite[addr[i].strip().replace('\n','').replace(' ','')]=[price[i].strip().replace('\n','').replace(' ',''),site[i].strip().replace('\n','').replace(' ','')]
			if '免费' in price[i]:
				prices="free"
	else:
		allsite="NO site see"
		#print("NO site see")
	return allsite,prices

if __name__=="__main__":
	begin=time.time()
	main_url='https://movie.douban.com/top250'
	cll=mongodb_connect()
	get_content(main_url)
	end=time.time()
	print('花费的总时间为：%s\r' % int(time.time()-begin))
