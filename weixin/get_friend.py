import itchat
import random
import time
itchat.auto_login(enableCmdQR=-2)
time.sleep(30)
while True:
	x=''
	for i in range(3):
		x+=random.choice('zyxwvutsrqponmlkjihgfedcba')
	itchat.add_friend('zjhz'+x)
	
