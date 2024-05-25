"""
https://zhuanlan.zhihu.com/p/643800469
5
REQUEST=10
REQUEST=20
RELEASE=0
REQUEST=20
REQUEST=10

记录已申请的内存即可
申请时遍历已申请的内存，获取可分配的空间，如果无法分配继续寻找更新首地址为止
"""


def release_mem(mem_addr, malloc_mem):
	idx = -1
	for i in range(len(malloc_mem)):
		if mem_addr == malloc_mem[i][0]:
			idx = i
			break
	if idx == -1:
		print("error")
	else:
		malloc_mem.pop(idx)


def request_mem(mem_size, malloc_mem):
	addr = 0
	insert_idx = 0
	for m in malloc_mem:
		if m[0] > addr and (m[0] - addr) >= mem_size:
			# 寻找插入位置
			malloc_mem.insert(insert_idx, [addr, addr + mem_size - 1])
			return addr
		else:
			addr = m[1] + 1
			insert_idx += 1
	if addr > 100:
		print("error")
	else:
		print(addr)


if __name__ == '__main__':
	command_count = int(input())
	commands = [input() for _ in range(command_count)]
	mem_size = 100
	
	malloc_mem = [[mem_size, mem_size + 1]]
	for c in commands:
		tmp = c.split('=')
		cmd = tmp[0]
		m = int(tmp[1])
		if cmd == 'RELEASE':
			release_mem(m, malloc_mem)
		if cmd == 'REQUEST':
			addr = request_mem(m, malloc_mem)
			print(addr)
