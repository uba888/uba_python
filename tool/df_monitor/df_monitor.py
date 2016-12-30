#!/usr/bin/python3

import time
import pymongo
from os import statvfs

df_list=['/','/alidata']
ip='114.55.228.9'
clt_mongo=pymongo.MongoClient('114.55.228.9',27017)
clt_mongo.admin.authenticate('clickplus','Jdyun1234')
clt=clt_mongo.zabbix.dfinfo

def df_use(path):
	df_root=statvfs(path)
	avail=df_root.f_bavail*df_root.f_bsize/(1024*1024*1024)
	Size=df_root.f_bsize*df_root.f_blocks/(1024*1024*1024)
	use=int((Size-avail)*100/Size)
	return use,int(Size-avail)


def df_all():
	df={}
	df['sysid']=ip
	df['_id']=time.strftime("%Y%m%d",time.localtime(time.time()))+"+"+ip
	for i in df_list:
		df['df_'+i[1:]],df['df_'+i[1:]+'_size']=df_use(i)
	return df

def get_df():
	df={}
	df['_id']=str(time.strftime("%Y%m%d",time.localtime(time.time()-60*60*24)))+"+"+ip
	df['sysid']=ip
	dfinfo_old=clt.find_one(df)
	return dfinfo_old


#def judge_df(df_old,df_new):
	cha_=df_new['df_']-df_old['df_']
	cha_alidata=df_new['df_alidata']-df_old['df_alidata']
	if cha_ >3 or cha_alidata>3:
		text="%s的/目录涨%d;alidata涨%d" % (ip,cha_,cha_alidata)
		#短信报警		
	
	else:
		print("%s的/目录涨了%d百分点;alidata涨了%d百分点" % (ip,cha_,cha_alidata))
df =df_all()
print(df)
try:
	clt.insert_one(df)
except pymongo.errors.DuplicateKeyError:
	pass
	
#df_old=get_df()
#judge_df(df_old,df)
	
		

