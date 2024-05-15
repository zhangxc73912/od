"""
https://blog.nowcoder.net/n/c7bb482cddb647b5965c2f55ef13f7da

1 a键在屏幕上输出一个字母 a;
2 ctrl-c将当前选择的字母复制到剪贴板;
3 ctrl-x将当前选择的 字母复制到剪贴板，并清空选择的字母;
4 ctrl-v将当前剪贴板里的字母输出到屏幕;
5 ctrl-a 选择当前屏幕上所有字母。
"""

if __name__ == '__main__':
	data = input()
	screen = ''
	copy_data = ''
	for char in data:
		is_selected = False
		if char == '1' and is_selected:
			is_selected = False
			screen = 'a'
		elif char == '1' and not is_selected:
			screen += 'a'
		elif char == '2' and is_selected and screen:
			copy_data = screen
		elif char == '3' and is_selected and screen:
			copy_data = screen
			screen = ''
			is_selected = False
		elif char == '4' and is_selected and copy_data:
			is_selected = False
			screen = copy_data
		elif char == '5' and screen:
			is_selected = True
	
	print(len(screen))
			
		