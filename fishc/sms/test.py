# -*- coding: utf-8 -*-
import top.api
url='gw.api.taobao.com'
port='80' 
appkey='23476704'
secret='ae160cb05b134f149289f625df0fae21'
req = top.api.AlibabaAliqinFcSmsNumSendRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))
 
req.extend = "123456"
req.sms_type = "normal"
req.sms_free_sign_name = "活动验证"
req.sms_param = "{content:'test'}"
req.rec_num = "18657173220"
req.sms_template_code = "SMS_16720329"
try :
     resp = req.getResponse()
     print (resp)
except Exception,e:
     print (e)
