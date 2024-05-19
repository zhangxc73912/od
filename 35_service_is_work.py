"""
https://zhuanlan.zhihu.com/p/645146250

a1-a2,a5-a6,a2-a3
a5,a2
"""

def update_nodes_status(fault_node, nodes_status, relation_map):
	nodes_status[fault_node] = False
	if fault_node in relation_map:
		nodes_status[fault_node] = False
		update_nodes_status(relation_map[fault_node], nodes_status, relation_map)


if __name__ == '__main__':
	relations = input().split(',')
	fault_nodes = input().split(',')
	nodes_status = {}
	relation_map = {}
	nodes = set()
	normal_nodes = []
	for r in relations:
		tmp = r.split('-')
		nodes.add(tmp[0])
		nodes.add(tmp[1])
		relation_map[tmp[1]] = tmp[0]
		
	for n in nodes:
		nodes_status[n] = True
	
	for fault_node in fault_nodes:
		update_nodes_status(fault_node, nodes_status, relation_map)
	
	for n in nodes_status:
		if nodes_status[n]:
			normal_nodes.append(n)
	
	if len(normal_nodes) > 0:
		print(','.join(normal_nodes))
	else:
		print(',')
