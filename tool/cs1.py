import urllib.request
import re  
import json  
  
class Youdao:  
    def __init__(self):  
        self.url = 'http://fanyi.youdao.com/openapi.do'  
        self.key = '695028818' #有道API key  
        self.keyfrom = 'nicomochina' #有道keyfrom  
  
    def get_translation(self,words):  
        url = self.url + '?keyfrom=' + self.keyfrom + '&key='+self.key + '&type=data&doctype=json&version=1.1&q=' + words
        page = urllib.request.urlopen(url)
        result = page.read().decode("utf8")
        json_result = json.loads(result)  
        json_result = json_result["translation"]  
        for i in json_result:  
            print(i)  
  
youdao = Youdao()  
while True:
    msg = input('请输入单词\句子（输入quit结束）:')  
    if msg == 'quit':  
        break  
    youdao.get_translation(msg)

