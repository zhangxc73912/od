"""
https://www.nowcoder.com/questionTerminal/5382ff24fbf34a858b15f93e2bd85307

https://blog.csdn.net/SD_JZZ/article/details/132301654
"""

if __name__ == '__main__':
	sub_string = input()
	parent_string = input()
	
	sub_string_length = len(sub_string)
	parent_string_length = len(parent_string)
	sub_string_index = 0
	is_substring = False
	
	for c in parent_string:
		if c == sub_string[sub_string_index]:
			sub_string_index += 1
		if sub_string_index == sub_string_length:
			is_substring = True
			break
			
	print(str(is_substring).lower())