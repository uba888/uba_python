#!/usr/bin/python3
import os
import time
'''读取章节
'''	
def get_book(path): 
	os.chdir(path)
	zhang=os.listdir('.')
	zhang.sort()
	zhang_dict={}
	while True:
		for i in range(len(zhang)):
			zhang_dict[str(i)]=zhang[i]
			print("%s) %s" % (str(i),zhang[i]))
		print('''b) 返回上一层
q) 退出''')			
		num=input("请输入要查看的章节:")
		if num=='q':
			break
		elif num=='b':
			os.chdir('..')
			new_path=os.getcwd()
			get_book(new_path)
		if os.path.isdir(zhang_dict[num]):
			new_path=os.path.join(path,zhang_dict[num])
			get_book(new_path)
		elif os.path.isfile(zhang_dict[num]):
			new_path=os.path.join(path,zhang_dict[num])
			read_book(new_path)
		
			

def read_book(path):
	with open(path,'r') as file:
		content=file.readlines()
		for i in content:
			if i.strip()=='':
				pass
			else:
				print(i)
				time.sleep(1)


if __name__=="__main__":
	books={"a":"藏地密码"}
	a=input('''当前的小说有
a) 藏地密码
请输入对应编号进行阅读:''')
	name=books[a]
	book_path=os.path.join(os.getcwd(),name)
	get_book(book_path)
