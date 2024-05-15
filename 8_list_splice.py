"""
https://zhuanlan.zhihu.com/p/645410908
3
2
2,5,6,7,9,5,7
1,7,4,3,4

4
3
1,2,3,4,5,6
1,2,3
1,2,3,4
"""

if __name__ == '__main__':
	substring_length = int(input())
	list_count = int(input())
	lists = [list(map(int, input().split(','))) for i in range(list_count)]
	
	res = []
	while len(lists) > 0:
		for i in range(len(lists)):
			arr = lists[i]
			if len(arr) >= substring_length:
				res.extend(arr[:substring_length])
				arr = arr[substring_length:]
			else:
				res.extend(arr)
				arr = []
			lists[i] = arr
		lists = [arr for arr in lists if len(arr) > 0]
	
	print(",".join(map(str, res)))
