class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data string字符串
# @return TreeNode类
#

class Solution:
	def buildTree(self, data):
		nodes = data.split(" ")
		if len(nodes) == 0:
			return None
		root = TreeNode(nodes[0])
		stack = [root]
		for i in range(1, len(nodes)):
			while len(stack) > 0:
				head = stack.pop()
				if head == None:
					i += 2
					continue
				left_node = self.buildNode(nodes[i])
				right_node = self.buildNode(nodes[i + 1])
				if left_node != None:
					head.left = left_node
				if right_node != None:
					head.right = right_node
				
				head.left = left_node
				stack.append(right_node)
				stack.append(left_node)
				i += 2
		
		return root


def buildNode(self, val):
	if val == "#":
		return None
	else:
		return TreeNode(val)