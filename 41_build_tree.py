class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def buildTree(self, data: str) -> TreeNode:
		nodes = data.split(" ")
		if len(nodes) == 0:
			return None
		root = self.buildNode(nodes[0])
		stack = [root]
		i = 1
		while i < len(nodes):
			head = stack.pop(0)
			if head == None:
				i += 2
				continue
			child_count = 2
			
			while child_count > 0 and i < len(nodes):
				child_count -= 1
				node = self.buildNode(nodes[i])
				i += 1
				
				if node == None:
					continue
				stack.append(node)
				
				if child_count == 1:
					head.left = node
				else:
					head.right = node
		
		return root
	
	def buildNode(self, val):
		if val == "#":
			return None
		else:
			return TreeNode(int(val))