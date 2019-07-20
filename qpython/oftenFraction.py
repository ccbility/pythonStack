import random

subject = {
	'142857':'1/7', '285714':'2/7', '428571':'3/7','571428':'4/7','714285':'5/7','857142':'6/7',
	'5':'1/2',
	'333':'1/3','666':'2/3',
	'25':'1/4', '75':'3/4',
	'1666':'1/6','3333':'2/6','8333':'5/6',
	'125':'1/8','375':'3/8','875':'7/8',
	'1111':'1/9',
}
key = list(subject.keys())
random.shuffle(key)

for i in key:
	print(i)
	ans = input("答案:")
	item = subject.get(i)
	rAns = item
	if(ans == rAns):
		print('right')
	else:
		print('wrong，答案是：' + rAns)