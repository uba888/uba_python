#!/usr/bin/python3

import requests
import hashlib
from scrapy import Selector
import http.cookiejar as cookielib

# 构造 Request headers
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
session=requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
	session.cookies.load(ignore_discard=True)
except:
	print("Cookie 未能加载")

# 模拟登陆
def login(username,password):
	password=hashlib.md5(password.encode('utf-8')).hexdigest()
	kgc_url='http://www.kgc.cn/member/login?redirect_url=http%3A%2F%2Fwww.kgc.cn%2F'
	kgc_data={'UserLoginForm[redirect_url]': 'http://www.kgc.cn/', 'UserLoginForm[password]':password, 'UserLoginForm[username]':username}
	session.get(kgc_url)
	response=session.post(kgc_url,data=kgc_data,headers=headers)
	xp=Selector(text=response.text)
	username=xp.xpath('//span[@class="top-nick"]/text()').extract()
	try:
		username[0]
		print("欢迎%s登陆成功" % (username[0]))
	except:
		print("登陆失败")
	session.cookies.save()	
# 修改个人信息
def personal_set():
	config_headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
	config_url='http://www.kgc.cn/my/member/modifyProfile'
	realname=input('请输入您要修改的姓名:')
	sign=input('请输入您要设置的个性签名:')
	config_data={'sign': sign, 'realname':realname}
	r3=session.post(config_url,data=config_data,headers=config_headers)
	try:
		print(r3.json())
		print("修改成功")
	except:
		print("未修改成功，请检查")

#查询个人信息
def select():
	config_headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
	response=session.get('http://www.kgc.cn/my/member/profile.shtml#self-zl',headers=config_headers)
	hxs=Selector(text=response.text)
	old_realname=hxs.xpath('//div[@class="self-zl self-common hide"]/form/div[1]/input/@value').extract()
	old_sign=hxs.xpath('//div[@class="self-zl self-common hide"]/form/div[7]/input/@value').extract()
	print("现在的姓名为：%s,现在的个性签名为：%s" % (old_realname,old_sign))

if __name__=="__main__":
	while True:
		print('''=================请选择相应菜单进行操作=================
1) 进行登陆
2) 修改个人信息
3) 查询个人信息
4) 退出菜单''')
		choice=input("请选择你要进行的操作:")
		if choice == "1":
			username=input('请输入用户名:')
			password=input('请输入密码:')
			login(username,password)
		elif choice == "2":
			personal_set()
		elif choice == "3":
			select()	
		elif choice == "4":
			print("谢谢使用!")
			break
		else:
			print("输入错误，请重试")

	
