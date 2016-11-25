a=120
b=194
cb=120
s=1
c=1
cuo=int(input('please input cuo:'))
while s<=cuo:
	for c in range(1,100):
		win=74*c-cb
		if win>=s*50:
			print(c)
			break	
	s+=1
	cb=cb+c*120
	print(cb)
	
	 

