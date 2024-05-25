class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next


def reverse(root):
	tmp = root
	pre = Node(0)
	while tmp != None:
		node = tmp
		tmp = tmp.next
		node.next = pre.next
		pre.next = node
	
	return pre.next


def load_link(s):
	root = Node(0)
	tmp = root
	s = s.lstrip("{")
	s = s.rstrip("}")
	for d in s.split(","):
		node = Node(d)
		tmp.next = node
		tmp = tmp.next
	return root.next


def print_link(root):
	res = []
	while root != None:
		res.append(root.val)
		root = root.next
	print("{" + ",".join(res) + "}")


if __name__ == "__main__":
	data = input()
	root = load_link(data)
	root = reverse(root)
	print_link(root)
