#!/usr/bin/env python
#encoding:utf-8
#此脚本用处是给外网锁定用户随机生成8位字母数字的密码，并给内网发送账号密码邮件

import smtplib
import random
import sys
import time
from email.mime.text import MIMEText
from email.utils import formataddr

user_file='/test/test/824/userlist' #用户列表文件，存放user_id，一行一个user_id
filetime=time.strftime('%Y%m%d')
user_pwd='/test/test/824/user_pwd'+filetime  #存放user_id和密码的文件，执行脚本后根据此文件修改外网账号密码，也可以在此脚本中添加修改密码的命令
def userpwd():
    with file(user_file,'r') as user_f:
        for line in user_f.readlines():
            user=line.strip()
            pwd=ran(8) #调取ran(s)函数，取8位随机数，可按需修改
            up=user+"    "+pwd
            sendmail(user,pwd)
            with file(user_pwd,'a') as pwd_f:
                pwd_f.write(up+"\n")
def sendmail(user,pwd):
    to=user+'@163.com' #需替换成杭州银行内网域名@hzbank.com
    subject='外网邮箱账号已开通'
    contect='外网邮箱账号为:'+to+';外网邮箱密码为:'+pwd
    send(to,subject,contect)
def send(to,subject,contect):
        print(to,subject,contect)
        msg = MIMEText(contect, 'plain', 'utf-8')
        msg['From'] = formataddr(["uba",'uba2016@163.com'])#信头，改写成内网发信账号
        msg['To'] = formataddr([to,to])
        msg['Subject'] = subject
        server = smtplib.SMTP("smtp.163.com", 25)#改成内网ip
        server.login("uba2016@163.com", "uba2016")#内网发信账号
        server.sendmail('uba2016@163.com', [to,], msg.as_string())#改写内网发信账号
        server.quit()
def ran(s):
        x=''
        for i in range(s):
                x+=random.choice('zyxwvutsrqponmlkjihgfedcba1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')#定义随机字符库，A-Z,a-z,0-9可按需修改
        return(x)
if __name__=='__main__':
    userpwd()
