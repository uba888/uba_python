# coding=utf-8
import urllib.request
import urllib.parse

url = "https://ca.aliyuncs.com/gw/alidayu/sendSms" \
	+ "?rec_num=18657173220" \
	+ "&sms_template_code=SMS_16720329" \
	+ "&sms_free_sign_name=xxx" \
	+ "&sms_type=normal" \
	+ "&extend=1234" \
	+ '&sms_param={"content":"test"}'
print(url)
req = urllib.request.Request(url)
req.add_header("X-Ca-Key", "23469296")
req.add_header("X-Ca-Secret", "89772694c9405a741f4a3c1d246004b9")
resp = urllib.request.urlopen(req)
content = resp.read()
if content:
	print(content)
