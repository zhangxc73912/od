"""
https://www.nowcoder.com/discuss/618014262505627648?sourceSSR=search

5
-5
-5 1 6 0 -7

2
1
-5 1
"""


def is_validate(luck_num, commands, command_count):
	if luck_num < -100 or luck_num > 100:
		return False
	
	if command_count < 1 or command_count > 100:
		return False
	
	if command_count != len(commands):
		return False
	
	for c in commands:

		if c < -100 or c > 100:
			return False
	return True

def add_luck_num(move_step, luck_num):
	if move_step == luck_num:
		if move_step > 0:
			move_step = move_step + 1
		else:
			move_step = - (-move_step + 1)
	return move_step


def move(luck_num, commands, command_count):
	current = 0
	for i in range(command_count):
		move_step = commands[i]
		if move_step == luck_num:
			if move_step > 0:
				move_step = move_step + 1
			else:
				move_step = - (-move_step + 1)
		current += move_step
		commands[i] = current
	commands.append(0)
	return max(commands)


if __name__ == '__main__':
	command_count = int(input())
	luck_num = int(input())
	commands = list(map(int, input().split(' ')))
	if is_validate(luck_num, commands, command_count):
		print(move(luck_num, commands, command_count))
	else:
		print('12345')
