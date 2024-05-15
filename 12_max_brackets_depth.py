"""
https://zhuanlan.zhihu.com/p/643934425

[]
([]{()})
([](){()})
(]
([)[
)(
(()()()()())
"""

def get_depth(data):
	source_data = {
		']': '[', '}': '{', ')': '(',
	}
	
	stack = []
	depth = 0
	max_depth = 0
	for char in data:
		# 命中左括号从栈取出一个，否则入栈，栈当前的元素数量为深度
		if char in source_data:
			if len(stack) == 0:
				return 0
			tmp = stack.pop()
			if source_data[char] != tmp:
				return 0
			
			depth += 1
			max_depth = max(max_depth, depth)
		else:
			stack.append(char)
			depth = 0
	
	if len(stack) > 0:
		return 0
	
	return max_depth


if __name__ == '__main__':
	data = input()
	print(get_depth(data))
