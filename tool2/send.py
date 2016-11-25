#!/usr/bin/env python
#encoding:utf-8
from smtp import send
def sendmail():
	to='lsqtyihui@163.com'
	subject='报警'
	contect='this is测试 a test2'
	send(to,subject,contect)
if __name__=='__main__':
	sendmail()
