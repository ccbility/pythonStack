import random


def getBitNum(bit):
	min = "1" + "0" * (bit - 1)
	max = "9" * bit

	return random.randint(int(min), int(max))