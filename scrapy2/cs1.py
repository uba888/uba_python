import requests
from scrapy import Selector

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
            print(price[i])
            print(type(price[i]))
            if '付费' in price[i]:
                prices="free"
                print(prices)
    else:
        allsite="NO site see"
        #print("NO site see")

get_addr('https://movie.douban.com/subject/1291546/')
