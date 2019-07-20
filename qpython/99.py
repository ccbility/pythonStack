import random

small = [2,3,4,5,6,7,8,9]
random.shuffle(small)

for i in small:
	tmp = [x for x in range(i,10)]
	random.shuffle(tmp)
	for j in tmp:
		print(str(j) + ' * ' + str(i))
		rAns = str(i * j)
		userAns = input('答案:')
		if(rAns == userAns):
			print('right')
		else:
			print('wrong，答案是' + rAns)