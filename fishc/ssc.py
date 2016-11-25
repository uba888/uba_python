a=[]
for i in range(10):
	for j in range(10):
		if not i%2 or not j%2:
			b=str(i)+str(j)
			c=int(b)
			a.append(c)
print(len(a))
print(a)	
