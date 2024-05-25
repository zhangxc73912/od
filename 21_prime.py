"""
https://zhuanlan.zhihu.com/p/645567916


核心如何判断素数，然后在遍历寻找即可
开平发计算一般的数据即可，减少遍历

判断素数的方式：除1和自身外没有其他因子
"""
import math


def is_prime(n):
	if n <= 3:
		return n > 1
	
	if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
		return False
	
	for i in range(5, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	
	return True
