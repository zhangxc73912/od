"""
https://zhuanlan.zhihu.com/p/645019220
4
0 3
1 3
3 5
3 6

4
0 3
1 4
4 7
5 8

2
1 2
3 4


"""

if __name__ == '__main__':
	n = int(input())
	data = []
	for i in range(n):
		data.append(list(map(int, (input().split(' ')))))
	
	res = []
	data.sort(key=lambda x: x[0])
	for i in range(n):
		for j in range(i + 1, n):
			if data[j][0] <= data[i][1]:
				x = data[j][0]
				y = min(data[i][1], data[j][1])
				res.append((x, y))
			else:
				# 按照x排序，所以后面的元素都大于y
				break
	if len(res) == 0:
		print('None')
	else:
		new_res = []
		pre = res[0]
		res.sort(key=lambda x: (x[0], -x[1]))
		for i in range(len(res)):
			if res[i][0] <= pre[1]:
				pre = [pre[0], max(pre[1], res[i][1])]
			else:
				new_res.append(pre)
				pre = res[i]
		
		new_res.append(pre)
		
		for i in new_res:
			print(i[0], i[1])
