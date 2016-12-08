#!/usr/bin/env python
# -*- coding: utf-8 -*-
import top.api
import sys
url='gw.api.taobao.com'
port='80'
appkey='23476704'
secret='ae160cb05b134f149289f625df0fae21'
req = top.api.AlibabaAliqinFcSmsNumSendRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))
def sendmsg(text,phonenum):
	req.extend = "123456"
	req.sms_type = "normal"
	req.sms_free_sign_name = "大鱼测试"
	req.sms_param = "{content:'%s'}" % text
	print("报警内容：%s" % req.sms_param)
	req.rec_num = phonenum
	req.sms_template_code = "SMS_16720329"
	try :
		resp = req.getResponse()
		print("短信发送返回码:%s" % resp)
	except Exception as e:
		pass
		print("短信发送返回码:%s" % e)

if __name__=="__main__":
	sendmsg(sys.argv[2],sys.argv[1])
