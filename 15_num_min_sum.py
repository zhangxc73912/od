"""
https://zhuanlan.zhihu.com/p/645486073

思路：正数按照个位处理，负数按照整体处理
负数判断标准 '-'
判断数字标准  '0' <= char <= '9'
及时更新符号

b1234a
bb12-34aa
"""


def update(nums, sum):
	tmp_sum = 0
	for i in range(len(nums)):
		tmp_sum = nums[i] + tmp_sum * 10 ** i
	sum -= tmp_sum
	return sum


if __name__ == '__main__':
	data = input()
	
	sum = 0
	is_negative = False
	nums = []
	for char in data:
		# 数字
		if char >= '0' and char <= '9':
			n = int(char)
			if is_negative:
				nums.append(n)
			else:
				sum += int(n)
		else:
			if char == '-':
				is_negative = True
			else:
				is_negative = False
			sum = update(nums, sum)
			nums = []
	# 以数字结尾需要处理
	sum = update(nums, sum)
	print(sum)
