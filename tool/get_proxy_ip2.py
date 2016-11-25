import requests
import random
from scrapy import Selector

ipk=[]
portk=[]
ipport=[]
xyk=[]
def url():
	for i in range(10):
		url="http://www.kuaidaili.com/proxylist/%s/" % str(i+1)
		get_proxy(url)

def get_proxy(url):
	text=requests.get(url)
	hxs=Selector(text=text.text)
	ip=hxs.xpath('//*[@id="index_free_list"]/table/tbody/tr/td[1]/text()').extract()
	port=hxs.xpath('//*[@id="index_free_list"]/table/tbody/tr/td[2]/text()').extract()
	xy=hxs.xpath('//*[@id="index_free_list"]/table/tbody/tr/td[4]/text()').extract()	

	if len(ip)==len(port):
		for i in range(len(ip)):
			if 'HTTPS' in xy[i]:
				xyk.append("https")
			else:
				xyk.append("https")
			ipk.append(ip[i])
			portk.append(port[i])
			ipport.append(ip[i]+":"+port[i])


if __name__=="__main__":
	url()
#	print(len(ipk),len(portk),len(ipport),len(xyk))
#	print(ipk,portk,ipport,xyk)			
	a=random.randint(0,100)
	proxy={}
	proxy[xyk[a]]="http://"+str(ipk[a])+":"+str(portk[a])
	proxy['http']="http://"+str(ipk[a])+":"+str(portk[a])
	print(proxy)
	r=requests.get("http://monitor.clickplus.cn/zabbix",proxies=proxy)
