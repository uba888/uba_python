#!/usr/bin/env python
#encoding utf-8
filename=input("please input filename:")
with open(filename) as file1:
    file1_text=file1.read()
while True:
	old=input("please input old:")
	new=input("please input new:")
	if old in file1_text:
		a=file1_text.split(old)
		num=len(a)-1
		print("文件%s 中共有%d个%s" % (filename,num,old))
		print("您确定要把所有的%s替换为%s么？" % (old,new))
		ans=input("【yes/no】:")
		break
	else:
		print("文件中没有此字符，请重新输入")

if ans=='yes':
	newtext=file1_text.replace(old,new)
	with open(filename,'w') as file2:
		file2.write(newtext)
		print("替换成功")
else:
	print("字符没有替换")	
