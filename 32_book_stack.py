"""
https://zhuanlan.zhihu.com/p/526649048

[[20,16],[15,11],[10,10],[9,10]]

[[20,16],[15,11],[8,8],[9,6],[7,7]]

1. 书籍排序规则，按照体积排序（如果按照长 宽排序会漏掉数据）
2. 记录上次放置的书籍

答案提示中 长宽比要求，不太清楚原因(and 0.67 < books[i][0] / books[i][1] < 1.5)
"""

if __name__ == '__main__':
	books = input()
	books = eval(books)
	books = sorted(books, key=lambda book: book[0] * book[1], reverse=True)
	max_book_count = 1
	last_book = books[0]
	for i in range(1, len(books)):
		if last_book[0] > books[i][0] and last_book[1] > books[i][1]:
			max_book_count += 1
			last_book = books[i]
	print(max_book_count)
