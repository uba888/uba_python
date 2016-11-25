#!/usr/bin/env python
#求最大公约数
import re
def gcd(x,y):
	if x>y:
		p=x
		q=y
	else:
		p=y
		q=x
	while True:
		a=divmod(p,q)
		if a[1]==0:
			big=q
			break
		else:
			p=q
			q=a[1]

	return big
'''
def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t

    return x
    
print(gcd(4, 6))
'''
#十进制转二进制
def tzt(x):
	t=1
	z='0b'
	y=''
	while t==1:
		a=divmod(x,2)
		y=str(a[1])+y
		if a[0]>0:
			x=a[0]
		else:
			t=0		
	
	return z+y
		
def sumArgs(*args,base=3):
	'打印参数的和乘base'
	sum=0
	for i in args:
		sum+=int(i)
	print(sum*base)

'''
#查水仙花
for i in range(100,1000):
	b=i//100
	s=i%100//10
	g=i%10
	if b**3+s**3+g**3==i:
		print("花儿:"+str(i))
'''


'''
def findstr(par,son):
	re1=son
	xx=re.findall(re1,par)
	ci=len(xx)
	return ci
par=input("please input par:")
son=input("please input son")
a=findstr(par,son)
print('son in par is'+str(a)+'ci')
'''
'''
def findStr(desStr, subStr):
    '找相同字符串'
	count=0
	length=len(desStr)
    if subStr not in desStr:
        print('在目标字符串中未找到字符串!')
    else:
        for each1 in range(length-1):      
            if desStr[each1] == subStr[0]:
                if desStr[each1+1] == subStr[1]:
                    count += 1
                    
        print('子字符串在目标字符串中共出现 %d 次' % count)
'''

'''
desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串(两个字符)：')
findStr(desStr, subStr)
'''

def countZf(*xx):
	'统计字母数字空格个数'
	x=len(xx)
	for y in range(x):
		zm=sz=kg=qt=0
		for i in xx[y]:
			if i.isalpha():
				zm+=1
			elif i.isdigit():
				sz+=1
			elif i==' ':
				kg+=1
			else:
				qt+=1
		print('this is %d and zm %d and sz %d  and kg %d qita %d' % (y,zm,sz,kg,qt))


#countZf('you are 888 bitch !@@','asd')



'''
#统计文本中各字符串出现的次数
with open('string.txt','r') as string:
	zf=string.read()
	all=len(zf)
	allzf=''
	for i in range(all):
		if zf[i] not in allzf:
			allzf=allzf+zf[i]
	x=[0]
	cd=len(allzf)
	print(cd)
	x=x*cd	
	print(x)
	for i in range(all):
		for j in range(cd):
			if zf[i]==allzf[j]:
				x[j]+=1	
	print(allzf,x)		
'''

'''
#字符统计
with open('string2.txt','r') as string2:
	DD='QWERTYUIOPASDFGHJKLZXCVBNM'
	dd='qwertyuiopasdfghjklzxcvbnm'
	zf=string2.read()
	all=len(zf)
	x=''
	for i in range(3,all-4):
		#xx1=zf[i-3:i]
		#xx2=zf[i+1:i+4]
		#xx3=xx1+xx2
		#print(xx3)
		#if all(xx4 in DD for xx4 in xx3):



		if (zf[i] in dd) and (zf[i-1] in DD) and (zf[i-2] in DD) and (zf[i-3] in DD) and (zf[i+1] in DD) and (zf[i+2] in DD) and (zf[i+3] in DD) and (zf[i+4] in dd) and (zf[i-4] in dd):
			x=x+zf[i]
	print(x)	
'''	
		
		
def gcd1(x,y):
	if y==0:
		#print(x)
		s=x
		print(s)
		return x
		
	else:
		a=divmod(x,y)
		x,y=y,a[1]
		return gcd(x,y)

def xxoo(x):
	if x==2:
		return 1
	elif x==1:
		return 1
	else:
		return xxoo(x-1)+xxoo(x-2)
	
	
def hanot(n,x,y,z):

	if n==1:
		print(':',x,"---->",z)
	else:
		hanot(n-1,x,z,y)
		print(':',x,"---->",z)
		hanot(n-1,y,x,z)

def bin1(x):
	s=''
	if x:
		s=bin1(x//2)
		s=s+str(x%2)
		return s
	else:
		
		return s
	
n=int(input('please input n:'))
#x=input('please input x:')
#y=input('please input y:')
#z=input('please input z:')
a=bin1(n)
print(a)


