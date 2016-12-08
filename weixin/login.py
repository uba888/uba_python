#!/usr/bin/python
#encoding=utf-8
import requests
import re
import sys
import time
import os
import json
from PIL import Image
from scrapy import Selector

session=requests.session()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
BLOCK = u'\u2588'


def get_uuid():
	url="https://login.weixin.qq.com/jslogin"
	params={'appid':'wx782c26e4c19acffb','fun':'new'}
	r1=session.get(url,headers=headers,params=params)
	rules='window.QRLogin.uuid = "(.+?)";'
	uuid=re.search(rules,r1.text).group(1)
	return uuid

def get_QR(uuid):
	url='https://login.weixin.qq.com/qrcode/%s' % uuid
	r2=session.get(url,stream=True,headers=headers)
	with open('QR.jpg','wb') as f: f.write(r2.content)

def open_QR(fileDir, size = 37, padding = 3,
        white = BLOCK, black = '  ', enableCmdQR = True):
    img     = Image.open(fileDir)
    times   = img.size[0] / (size + padding * 2)
    rgb     = img.convert('RGB')
    try:
        blockCount = int(enableCmdQR)
        assert(0 < abs(blockCount))
    except:
        blockCount = 1
    finally:
        white *= abs(blockCount)
        if blockCount < 0: white, black = black, white
    sys.stdout.write(' '*50 + '\r')
    sys.stdout.flush()
    qr = white * (size + 2) + '\n'
    startPoint = padding + 0.5
    for y in range(size):
        qr += white
        for x in range(size):
            r,g,b = rgb.getpixel(((x + startPoint) * times, (y + startPoint) * times))
            qr += white if r > 127 else black
        qr += white + '\n'
    qr += white * (size + 2) + '\n'
    sys.stdout.write(qr)
    check_login(uuid)

def check_login(uuid):
	url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login'
	params = 'tip=1&uuid=%s&_=%s' % (uuid, int(time.time()))
	r3=session.get(url, params=params, headers=headers)
	rules2='window.code=(.+?);'
	code=re.search(rules2,r3.text).group(1)
	#code 200 400 408 201
	if code=='200':
		os.remove('QR.jpg')
		dict=get_loginInfo(r3.text)
		print(dict['User']['NickName']+" login success")
		loging()
	elif  code=='201':
		while code=='201':
			code=check_login(uuid)
			time.sleep(2)
	else:
		print("login failed") 

def get_loginInfo(loginTxt):
	rules3=r'window.redirect_uri="(\S+)";'
	global loginInfo
	loginInfo['BaseRequest'] = {}
	loginInfo['url']=re.search(rules3,loginTxt).group(1)
	r4=session.get(loginInfo['url'],headers=headers,allow_redirects=False)
	xp=Selector(text=r4.text)
	loginInfo['url'] = loginInfo['url'][:loginInfo['url'].rfind('/')]	
	loginInfo['skey']=loginInfo['BaseRequest']['Skey']=xp.xpath('//skey/text()').extract()[0]
	loginInfo['wxsid']=loginInfo['BaseRequest']['Sid']=xp.xpath('//wxsid/text()').extract()[0]
	loginInfo['wxuin']=loginInfo['BaseRequest']['Uin']=xp.xpath('//wxuin/text()').extract()[0]
	loginInfo['pass_ticket']=loginInfo['BaseRequest']['DeviceID']=xp.xpath('//pass_ticket/text()').extract()[0]
	url='%s/webwxinit?r=%s' % (loginInfo['url'], int(time.time()))
	data = { 'BaseRequest': loginInfo['BaseRequest'], }
	r5=session.post(url,data=json.dumps(data),headers=headers)
	dict = json.loads(r5.content.decode('utf-8', 'replace'))
#	retrun dic['User']['UserName'],dic['User']['NickName']
	return dict

def sendMsg(user,msg):
	url = '%s/webwxsendmsg' % loginInfo['url']

def loging():
    while True:
        print('''=================请选择相应菜单进行操作=================
1) 查看消息
2) 给好友发消息
3) 找好友
4) 添加好友
q) exit
''')
        choice = raw_input("请选择你要进行的操作:")
        if choice == "1":
            print("正在查看消息")
        elif choice == "2":
            print("正在给好友发消息.....")
            user=raw_input("请输入好友id")
            msg=raw_input("请输入信息")
        elif choice == "3":
            print("正在查....")
        elif choice == "4":
            chatid=raw_input("请输入要添加的微信号")
        elif choice == "q":
            print("正在推出")
            break	

if __name__=="__main__":
	loginInfo={}
	uuid=get_uuid()
	get_QR(uuid)
	open_QR('QR.jpg',enableCmdQR=-2)
	while True:
		open_QR('QR.jpg',enableCmdQR=-2)
		print('''=================请选择相应菜单进行操作=================
1) 查看消息
2) 给好友发消息
3) 找好友
4) 添加好友
q) exit
''')
		choice = input("请选择你要进行的操作:")
		if choice == "1":
			print("正在查看消息")
		elif choice == "2":
			print("正在给好友发消息.....")
			user=input("请输入好友id")
			msg=input("请输入信息")
		elif choice == "3":
			print("正在查....")
		elif choice == "4":
			chatid=input("请输入要添加的微信号")
		elif choice == "q":
			print("正在推出")
			break
