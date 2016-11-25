#!/usr/bin/python2
#encoding:utf-8
import sys
import os
from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeSlowLogRecordsRequest


clt = client.AcsClient('YnJ8kOsszMXvmgBt','QHqm3JMjDalEbg2sqvEysG47kQMrq4','cn-hangzhou')

def get_pagecount(startdate,enddate):
	#传入查询初始时间和结束时间
	request = DescribeSlowLogRecordsRequest.DescribeSlowLogRecordsRequest()
	request.set_accept_format('json')
	request.set_DBInstanceId('rm-bp196ckqc2wi132y1')
	request.set_StartTime(startdate+'Z')
	request.set_EndTime(enddate+'Z')
	request.set_action_name('DescribeSlowLogs')
	request.set_PageSize(100)
	request.set_PageNumber(1)
	result = clt.do_action(request)
	return eval(result)['TotalRecordCount']

def get_record(startdate,enddate,pagenum):
	request = DescribeSlowLogRecordsRequest.DescribeSlowLogRecordsRequest()
	request.set_accept_format('json')
	request.set_DBInstanceId('rm-bp196ckqc2wi132y1')
	request.set_StartTime(startdate+'Z')
	request.set_EndTime(enddate+'Z')
	request.set_action_name('DescribeSlowLogs')
	request.set_PageSize(100)
	request.set_PageNumber(pagenum)
	result = clt.do_action(request)
	
	with open('MaxExecutionTime%s--%s.txt' % (startdate,enddate),'a+') as M_w:
		for i in eval(result)['Items']['SQLSlowLog']:
		#	if i['MaxExecutionTime']>1:
			M_w.writelines(str(str(i['MaxExecutionTime'])+"\t"+i['DBName']+"\t"+i['SQLText']+"\n"))
	with open('TotalExecutionTimes%s--%s.txt' % (startdate,enddate),'a+') as T_w:
		for i in eval(result)['Items']['SQLSlowLog']:
			#if i['MySQLTotalExecutionTimes']>1:
			T_w.writelines(str(str(i['MySQLTotalExecutionTimes'])+"\t"+i['DBName']+"\t"+i['SQLText']+"\n"))

if __name__=="__main__":
	#startdate=raw_input("请输入查询起始日期(2016-11-21):")
	#enddate=raw_input("请输入查询结束日期(2016-11-21):")
	startdate=sys.argv[1]
	enddate=sys.argv[2]
	allrecord=get_pagecount(startdate,enddate)
	for i in range(1,allrecord/100+2):
		get_record(startdate,enddate,i)
