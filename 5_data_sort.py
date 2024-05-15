"""
https://blog.csdn.net/cxh21627/article/details/125279439

3 4 256 257 258 259 260 261 262 263 264 265
"""


def get_remainder(d, b, c):
	# 转换16进制
	d16 = hex(d)[2:]
	
	# 补零
	if len(d16) % 2 != 0:
		d16 = '0' + d16
	
	# 按照步长为2进行叠加
	res = 0
	for i in range(0, len(d16), 2):
		res += int(d16[i:i + 2], 16)
	
	remainder = res % b
	if remainder < c:
		return remainder
	else:
		return -1


if __name__ == '__main__':
	data = list(map(int,input().split(' ')))
	c = data[0]
	b = data[1]
	data = data[2:]
	
	type_data = {}
	
	for d in data:
		remainder = get_remainder(d, b, c)
		if remainder != -1:
			if remainder in type_data:
				type_data[remainder] += 1
			else:
				type_data[remainder] = 1
	
	# 最多类型数目的值
	print(max(type_data.values()))
