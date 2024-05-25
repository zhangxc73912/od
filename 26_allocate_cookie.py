"""
https://www.nowcoder.com/discuss/594576774558683136?sourceSSR=search

1. 分配
2. 去除不符合条件的，分配方案
3. 去除重复的分配方案
"""

# 要求每人最少分配一个，所以可分配的苹果味m-n各
import copy


def allocate_cookie(cookie_count, people_count, ans, result):
	# 表示月饼已经分完了剩下的人接受的的是0
	if cookie_count <= 0:
		for i in range(people_count - 1, -1, -1):
			ans[i] = 0
		result.append(copy.deepcopy(ans))
		return
	
	# 分配到最后一人表示分配完成
	if people_count == 1:
		ans[people_count - 1] = cookie_count
		result.append(copy.deepcopy(ans))
		return
	
	for i in range(cookie_count + 1):
		ans[people_count - 1] = i
		allocate_cookie(cookie_count - i, people_count - 1, ans, result)


if __name__ == '__main__':
	people_count = int(input())
	cookie_count = int(input())
	if cookie_count - people_count < 0:
		print("0")
	else:
		ans = [0] * people_count
		result = []
		
		# 默认给每人先分一个饼干
		allocate_cookie(cookie_count - people_count, people_count, ans, result)
		
		# 获取合法结果
		validate_result = []
		for ans in result:
			deal_ans = copy.deepcopy(ans)
			deal_ans = list(set(deal_ans))
			deal_ans.sort(reverse=True)
			is_validate = True
			
			for i in range(len(deal_ans) - 1):
				if deal_ans[i] - deal_ans[i + 1] > 3:
					is_validate = False
					break
			if is_validate:
				# 加入的同时去重
				ans.sort()
				if ans not in validate_result:
					validate_result.append(ans)
		
		print(len(validate_result))
