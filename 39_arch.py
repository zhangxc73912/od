"""
https://blog.csdn.net/weixin_44052055/article/details/125772120

排列组合 采用回溯方式匹配。如果不符合，直接回退
"""


def dfs(arr, depth, used, ans, res):
	# 已经组合与原串长度一样
	if depth == len(arr):
		res.append(''.join(ans))
		return
	# 寻找下一个字符，进行匹配
	for i in range(len(arr)):
		if used[i]:
			continue
		
		# 去重关键点
		# 如果前一个字符与当前字符一样，不需要重新组合，判断标准前一个字符未被使用
		if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
			continue
		
		ans.append(arr[i])
		used[i] = True
		dfs(arr, depth + 1, used, ans, res)
		# 回退
		ans.pop()
		used[i] = False


if __name__ == '__main__':
	char_count = int(input())
	chars = input().split(' ')
	used = [False] * char_count
	res = []
	ans = []
	dfs(chars, 0, used, ans, res)
	print(res)
