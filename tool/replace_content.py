#!/usr/bin/python
# -*- coding=UTF-8 -*-

import sys
import os
def replace_content(*args):
	len_argv=len(args)
	#print '传参数量',len_argv-1

	if   len_argv <  3:
		print("参数错误 需要编辑的文件 被替换的字符串 提成成的字符串 [另存成的文件]")

	elif len_argv >  4:
		print("参数错误 需要编辑的文件 被替换的字符串 提成成的字符串 [另存成的文件]")

	else:
		if not os.path.isfile(args[0]):
			print('文件不存在')
			sys.exit()
		s_file  = open(args[0],'r+')
		old_str = args[1]
		new_str = args[2]
		d_file  = open(args[0]+'.tmp','w')
		for line in s_file.readlines():
			d_file.writelines(line.replace(old_str,new_str))
		s_file.close()
		d_file.close()

		if len_argv == 3:
			os.rename(args[0]+'.tmp',args[0])
		else:
			os.rename(args[0]+'.tmp',args[3])

replace_content('/test/test/fishc/xxx','ert','uba')
