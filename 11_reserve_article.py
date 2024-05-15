"""
https://zhuanlan.zhihu.com/p/645338552

I am a developer.
1
2

Hello world!
0
1

I am a developer.
0
3

Hello!
0
3
"""


def reserve_words(word_list):
	l = len(word_list)
	if l == 0:
		return word_list
	for i in range(int(l / 2)):
		word_list[i], word_list[l - i - 1] = word_list[l - i - 1], word_list[i]
	return word_list


if __name__ == '__main__':
	word_list = input().split(" ")
	l_idx = int(input())
	r_idx = int(input())
	new_word_list = word_list[:l_idx]
	new_word_list.extend(reserve_words(word_list[l_idx:r_idx + 1]))
	new_word_list.extend(word_list[r_idx + 1:])
	print(" ".join(new_word_list))
