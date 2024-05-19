"""
https://zhuanlan.zhihu.com/p/645549732

核心：当出现比前面小的数字，则把之前的数据进行剔除，如果提出到达预期则停止
2615371

存在0在首位的场景，需要主动剔除
"""

if __name__ == '__main__':
	data = input()
	cut_count = int(input())
	
	nums_stack = []
	for i in range(len(data)):
		while len(nums_stack) > 0 and cut_count > 0:
			if nums_stack[-1] > data[i]:
				nums_stack.pop()
				cut_count -= 1
			else:
				break
		nums_stack.append(data[i])
	
	# 未剔除需求字符串数量
	nums_stack = nums_stack[:len(nums_stack) - cut_count]
	
	# 去除0开头
	while len(nums_stack) > 0 and nums_stack[0] == '0':
		nums_stack.pop(0)
	print(''.join(nums_stack))
