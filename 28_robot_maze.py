"""
https://zhuanlan.zhihu.com/p/643171323

路径走过的点能够到达终点标记为2，无法到达标记为-1，未访问标记为0，墙的位置标记为1

6 4
5
0 2
1 2
2 2
4 1
5 1

6 4
4
2 0
2 1
3 0
3 1
"""


# 迷宫起始位置，可以行走的方向
def walk_maze(x, y, maze):
	maze_x = len(maze)
	maze_y = len(maze[0])
	
	# 越界不可达
	if x >= maze_x or y >= maze_y:
		return False
	
	# 已标记不可达不在继续
	if maze[x][y] == -1:
		return False
	
	# 坐标是墙不可达
	if maze[x][y] == 1:
		return False
	
	# 到达出口
	if maze[x][y] == 2:
		return True
	
	# 此路从未走过
	if maze[x][y] == 0:
		right = walk_maze(x + 1, y, maze)
		up = walk_maze(x, y + 1, maze)
		# 任意可达即可
		if right or up:
			maze[x][y] = 2
		else:
			maze[x][y] = -1
	
	return maze[x][y] == 2


if __name__ == '__main__':
	axis = list(map(int, input().split(' ')))
	wall_count = int(input())
	wall_axis = [list(map(int, input().split(' '))) for i in range(wall_count)]
	
	# 初始化并标记墙的位置
	maze = [[0 for j in range(axis[1])] for i in range(axis[0])]
	for pos in wall_axis:
		maze[pos[0]][pos[1]] = 1
	
	# 标记出口
	maze[axis[0]-1][axis[1]-1] = 2
	
	walk_maze(0, 0, maze)
	
	
	trap_count = 0
	unreachable_count = 0
	for i in range(axis[0]):
		for j in range(axis[1]):
			if maze[i][j] == 0:
				unreachable_count += 1
			elif maze[i][j] == -1:
				trap_count += 1
	
	print(trap_count, unreachable_count)
