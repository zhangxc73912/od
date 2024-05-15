"""
https://blog.nowcoder.net/n/ce4c0e4201c043c3b6dce8251613e654?from=nowcoder_improve

没有时间要求可以直接选择三层for循环，暴力解题
4 2 7 3 0
"""

if __name__ == '__main__':
	data = list(map(int, input().split(' ')))
	l = len(data)
	res = '0'
	data.sort(reverse=True)  # 做大的数放在最前面
	print(data)
	for i in range(l):
		for j in range(l):
			for k in range(l):
				if data[i] == data[j] + 2 * data[k] and i != k and i != j and j != k:
					res = " ".join([str(data[i]), str(data[j]), str(data[k])])
					break
	print(res)
