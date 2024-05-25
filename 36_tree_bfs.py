"""
题目描述：
有一棵二叉树，每个节点由一个大写字母标识(最多 26 个节点）。现有两组字母，分别表
示后序遍历（左孩子->右孩子->父节点）和中序遍历（左孩子->父节点->右孩子）的结果，
请输出层次遍历的结果。
输入描述：
输入为两个字符串，分别是二叉树的后续遍历和中序遍历结果。
输出描述：
输出二叉树的层次遍历结果。

后序 中序
CBEFDA CBAEDF

输出层序
ans = ABDCEF

1. 构建二叉树
2. 利用栈，逐层打印
"""


class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def buildTree(inorder, postorder):
	if len(postorder) == 0:
		return None
	if len(postorder) == 1:
		return TreeNode(inorder[0])
	root = TreeNode(postorder[-1])
	idx = inorder.index(postorder[-1])
	
	root.left = buildTree(inorder[:idx], postorder[:idx])
	root.right = buildTree(inorder[idx + 1:], postorder[idx:len(postorder) - 1])
	return root


def view_tree(root):
	result = []
	stack = [root]
	while stack:
		l = len(stack)
		while l > 0:
			node = stack.pop(0)
			result.append(node.val)
			l -= 1
			if node.left is not None:
				stack.append(node.left)
			if node.right is not None:
				stack.append(node.right)
	print(''.join(result))


if __name__ == '__main__':
	tree_input = input().split(' ')
	postorder = list(tree_input[0])
	inorder = list(tree_input[1])
	tree = buildTree(inorder, postorder)
	view_tree(tree)
