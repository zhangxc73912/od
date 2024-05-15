"""
https://zhuanlan.zhihu.com/p/645560084

dp数组存放偏移量
根据偏移量计算char
"""


def encrypt(s):
	s = list(s)  # 便于直接更新
	length = len(s)
	dp = [0 for _ in range(length)]
	for i in range(length):
		if i == 0:
			dp[i] = 1
		elif i == 1:
			dp[i] = 2
		elif i == 2:
			dp[i] = 4
		else:
			dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
		
		# 根据偏移量计算char
		s[i] = chr((dp[i] + (ord(s[i]) - 97)) % 26 + 97)
	
	print("".join(s))


if __name__ == '__main__':
	num = int(input())
	data = [input() for _ in range(num)]
	for d in data:
		encrypt(d)
