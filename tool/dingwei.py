#!/bin/usr/env python
#-*- coding:utf-8 -*-
'''百度地图API-高精度IP定位'''
import urllib2,json,threading
from Tkinter import *
code={161:'定位成功',167:'定位失败',1:'服务器内部错误',101:'AK参数不存在',200:'应用不存在，AK有误请检查重试',201:'应用被用户自己禁止',202:'应用被管理员删除',203:'应用类型错误',210:'应用IP校验失败',211:'应用SN校验失败',220:'应用Refer检验失败',240:'应用服务被禁用',251:'用户被自己删除',252:'用户被管理员删除',260:'服务不存在',261:'服务被禁用',301:'永久配额超限，禁止访问',302:'当天配额超限，禁止访问',401:'当前并发超限，限制访问',402:'当前并发和总并发超限',999:'网络连接错误---[内网或无网络连接]'}
def GetAddress(ip,ak='NtngTlqlcFnUmBzgr07ZOAjzqGmdZRmF'):
    try:
        res=urllib2.urlopen('http://api.map.baidu.com/highacciploc/v1?qcip=%s&qterm=pc&extensions=3&ak=%s&coord=bd09ll' % (ip,ak),timeout=2)
        resjson=json.loads(res.read())
        res.close()
        return resjson
    except Exception,e:        
        return 999
def main():
    text.delete(0.0,END)
    qip=ip.get()
    if qip is None:
        pass
    else:
        connectJson=GetAddress(qip)
        if connectJson != 999 and connectJson['result']['error'] == 161:
            formatted_address=connectJson['content']['formatted_address']#地址       
            confidence=connectJson['content']['confidence']#精准度
            if connectJson['content'].get('business'):
                business=connectJson['content']['business']#商圈       
            else :
                business=u'无'                       
            result=connectJson['result']['loc_time']#定位时间
            if connectJson['content'].get('location_description'):
                location_description=connectJson['content']['location_description']#精确到
            else :
                location_description=u'无'        
            text.insert(END,u'\nIP地址: %s    精准度: %0d%%\n\n'%(qip,float(confidence)*100))
            text.insert(END,u'所在地址: '+formatted_address+'\n\n')
            text.insert(END,u'所在商圈: '+business+'\n\n')
            text.insert(END,u'精确到: '+location_description+'\n\n')
            text.insert(END,u'定位时间: ['+result+']')
            codevar.set(code.get(connectJson['result']['error']))
        elif connectJson==999:
            codevar.set(code.get(connectJson))
        else:
            codevar.set(code.get(connectJson['result']['error']))
def SearchIP():
    t=threading.Thread(target=main)
    t.start()
if __name__ == '__main__':
    root=Tk()
    root.title(u'IP精准定位 <by Domenet 2016-10-11>')
    root.geometry("350x300")
    root.resizable(False, False)
    ip=StringVar()
    codevar=StringVar()
    lb=Label(root,text='待查询的IP地址:')
    ent=Entry(root,textvariable=ip,width=20)
    btn=Button(root,text=u'  查 询  ',command=SearchIP)
    text=Text(root,width=50,height=18)
    lb.grid(row=0,column=0,pady=5)
    ent.grid(row=0,column=1,pady=5)
    btn.grid(row=0,column=2,pady=5)
    text.grid(row=1,columnspan=3)
    codelb=Label(root,textvariable=codevar)
    codelb.grid(row=2,columnspan=3)
    codevar.set(u'准备就绪')
    mainloop()
    
