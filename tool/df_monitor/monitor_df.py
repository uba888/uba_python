#!/usr/bin/python3

import time
import pymongo
from os import statvfs
import os
#from sendsms import sendmsg
iplist=['114.55.228.9','114.55.110.179','120.27.158.46','118.178.240.170','120.27.146.30','114.55.4.124','47.90.36.23']
clt_mongo=pymongo.MongoClient('114.55.228.9',27017)
clt_mongo.admin.authenticate('clickplus','Jdyun1234')
clt=clt_mongo.zabbix.dfinfo


def judge_df(ip):
	df={}
	df['_id']=str(time.strftime("%Y%m%d",time.localtime(time.time())))+"+"+ip
	df['sysid']=ip
	df_new=clt.find_one(df)
	dfold={}
	dfold['_id']=str(time.strftime("%Y%m%d",time.localtime(time.time()-60*60*24)))+"+"+ip
	dfold['sysid']=ip
	df_old=clt.find_one(dfold)
	cha_=df_new['df_']-df_old['df_']
	cha_alidata=df_new['df_alidata']-df_old['df_alidata']
	if cha_ >3 or cha_alidata>3:
		text="%s的根目录涨了%d个百分点,alidata涨了%d个百分点" % (ip.rpartition('.')[2],cha_,cha_alidata)
		print(text)
		os.system("python2 sendsms.py 18657173220 %s" % text)

	else:
		pass

	if df_new['df_'] >70 or df_new['df_alidata'] >70:
		text="%s的根目录用了%d个百分点,alidata用了%d个百分点" % (ip.rpartition('.')[2],df_new['df_'],df_new['df_alidata'])
		os.system("python2 sendsms.py 18657173220 %s" % text)
	
if __name__=="__main__":
	for ip in iplist:
		judge_df(ip)

