#!/usr/bin/env python
import re

def check(passwd):
	sz=re.findall('\d',passwd)
	zm=re.findall('\w',passwd)
	r1=r'''\`|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\_|\+|\-|\=|\/|\*|\{|\}|\[|\]|\\|\||\'|\"|\;|\:|\/|\?|\,|\.|\<|\>'''			
	qp=re.findall(r1,passwd)
	if len(passwd)>16 and len(sz)*len(zm)*len(qp)!=0:	
		print('gao')
	elif len(passwd)>8 and (len(sz)*len(zm)!=0 or len(sz)*len(qp)!=0 or len(zm)*len(qp)!=0):
		print('zhong')
	elif len(passwd)<=8 or len(passwd)==len(sz) or len(passwd)==len(zm):
		print('ruo')
if __name__=='__main__':
	while True:	
		passwd=input("print q quit or please input:")
		if passwd!='q':
			check(passwd)
		else:
			break
	



 
