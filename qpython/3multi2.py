import tools

while True:
	num1 = tools.getBitNum(1)
	num2 = tools.getBitNum(3)

	print(str(num2) + " * " + str(num1))

	ans = str(num1 * num2)

	userAns = input("答案：")
	if(ans == userAns):
		print('right')
	else:
		print('wrong，答案是：' + ans)