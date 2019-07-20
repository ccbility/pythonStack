import tools

while True:
	num1 = tools.getBitNum(3)
	num2 = tools.getBitNum(3)

	print(str(num1) + " / " + str(num2))

	ans = str(num1 / num2 * 1000)[0:2]

	userAns = input("答案：")
	if(ans == userAns):
		print('right')
	else:
		print('wrong，答案是：' + ans)