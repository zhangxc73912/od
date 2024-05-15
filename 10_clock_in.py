"""
https://zhuanlan.zhihu.com/p/644967380

absent: 缺勤
late: 迟到
leaveearly: 早退
present: 正常上班.
现需根据员工出勤信息，判断本次是否能获得出勤奖，能获得出勤奖的条件如下
缺勤不超过一次
没有连续的迟到/早退,
任意连续 7 次考勤，缺勤/迟到/早退不超过 3 次

2
present
present absent present present leaveearly present absent
"""


def is_present(people_clock_statuses):
	absent_count = 0
	present_count = 0
	pre_clock_status = ""
	
	for idx in range(len(people_clock_statuses)):
		current_clock_status = people_clock_statuses[idx]
		if current_clock_status == 'absent':
			absent_count += 1
		
		# 缺勤不超过一次
		if absent_count > 1:
			return 'false'
		
		# 连续 迟到/早退
		if current_clock_status in ['late', 'leaveearly']:
			if pre_clock_status in ['late', 'leaveearly']:
				return 'false'
		
		if current_clock_status == 'present':
			present_count += 1
		
		# 计算7次考勤中否出出现3次异常
		if idx >= 6:
			if present_count < 4:
				return 'false'
			
			# 每次移动检测最前面的是否为present状态
			if people_clock_statuses[idx - 6] == 'present':
				present_count -= 1
		
		pre_clock_status = current_clock_status
	return 'true'


if __name__ == '__main__':
	people_num = int(input())
	people_clock_status_list = [input().split(" ") for i in range(people_num)]
	res = []
	
	for people_clock_statuses in people_clock_status_list:
		print(is_present(people_clock_statuses))
