"""
https://zhuanlan.zhihu.com/p/645339184
"""


def fn(n):
	if n == 0:
		return "1"
	return cal(fn(n - 1))


def cal(data):
	count = 0
	char = data[0]
	res = ''
	for idx in range(len(data)):
		# 如果字符串变化则需要变更，同时将计数清零
		if char != data[idx]:
			res += str(count) + char
			char = data[idx]
			count = 0
		
		count += 1
		
		if idx == len(data) - 1:
			res += str(count) + char
	
	return res


if __name__ == '__main__':
	num = int(input())
	print(fn(num))
