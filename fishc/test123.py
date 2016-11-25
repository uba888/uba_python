'''
                        贪心算法

需求：
    有一个背包，背包容量是M=150。有7个物品，物品可以分割成任意大小。
    要求尽可能让装入背包中的物品总价值最大，但不能超过总容量。
'''

goods = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [35, 30, 60, 50, 40, 10, 25]
price = [10, 40, 30, 50, 35, 40, 30]

count = 1
sumWeight = 0
BagSet = []

print('每次挑选物品中价值最大的物品装入背包。')

while True:
	ChoPri = max(price)
	flag_ChoPri = price.index(ChoPri)
	sumWeight += weight[flag_ChoPri]
	ChoGoods = goods[flag_ChoPri]
	BagSet.append(ChoGoods)
	if sumWeight <= 150:
		price[flag_ChoPri] = 0
		print('第%s次挑选过后' % count)
		print('此时背包的重量为%s。' % sumWeight)
		print('此时背包里面的物品有:')
		print(BagSet)
		print('---------------------------')
	else:
		print('第%s次挑选过后' % count)
		print('此时背包的重量为%s。' % sumWeight)
		print('此时背包里面的物品有:')	
		print(BagSet)
		print('贪心也要有个度！')
		break
	count+=1
