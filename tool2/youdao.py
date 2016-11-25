import urllib.request
import urllib.parse
import json

def youdao(content):
	url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
	data={}
	data['type']='AUTO'
	data['i']=content
	data['doctype']='json'
	data['xmlVersion']='1.8'
	data['keyfrom']='fanyi.web'
	data['ue']='UTF-8'
	data['action']='FY_BY_CLICKBUTTON'
	data['typoResult']='true'
	data=urllib.parse.urlencode(data).encode('utf-8')
	response=urllib.request.urlopen(url,data)
	html=response.read().decode('utf-8')
	ans=json.loads(html)
	result2=ans['smartResult']['entries'][1:]
#    result=str(result1)+str(result2)
	return result2
while True:
	content=input('please input:')
	if content=='quit!':
		break
	else:
		result=youdao(content)
		print('result is: %s' % result)

