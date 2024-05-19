"""
https://zhuanlan.zhihu.com/p/645553376
"""

if __name__ == '__main__':
	data = input()
	alpha_count = 0
	num_count = 0
	pre_idx = 0
	max_length = 0
	for idx in range(len(data)):
		if data[idx].isalpha():
			alpha_count += 1
			if alpha_count > 1:
				l = idx - pre_idx
				max_length = max(max_length, l)
				pre_idx = idx
		else:
			num_count += 1
	print(max_length)