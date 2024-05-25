"""
https://www.codeleading.com/article/43985735740/

1. 根据字符串构建二叉树
2. 遍历生成的二叉树

a{b{d,e{g,h{,I}}},c{f}}
"""


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def build_tree(data):
	t = TreeNode(data[0])
	tmp = t
	stack = [tmp]
	for i in range(1, len(data)):
		print(i)
		if data[i] == '{' and data[i + 1] != ',':  # 存在左节点
			i += 1
			node = TreeNode(data[i])
			stack.append(node)
			tmp.left = node
			tmp = tmp.left
		
		elif data[i] == ',':
			i += 1
			node = TreeNode(data[i])
			stack.pop()
			tmp = stack[-1]
			tmp.right = node
			tmp = tmp.right
			stack.append(node)
		
		elif data[i] == '}':  # 更新临时节点
			tmp = stack.pop()
		
		elif data[i] == '{' and data[i + 1] == ',':  # 不存在左节点
			i += 2
			node = TreeNode(data[i])
			stack.append(node)
			tmp.right = node
			tmp = tmp.right
	return t

def view_tree(root, result):
	if root.left:
		view_tree(root.left, result)
	result.append(root.val)
	if root.right:
		view_tree(root.right, result)


if __name__ == '__main__':
	data = input()
	tree = build_tree(data)
	result = list()
	view_tree(tree, result)
	print(''.join(result))
