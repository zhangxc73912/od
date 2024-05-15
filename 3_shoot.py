"""
https://blog.csdn.net/cxh21627/article/details/125221722
"""

if __name__ == '__main__':
	shoot_count = int(input())
	shoot_peoples = input().split(',')
	shoot_scores = input().split(',')
	
	shoot_people_scores = {}
	
	# 汇总射击者成绩
	for i in range(shoot_count):
		score = int(shoot_scores[i])
		if shoot_peoples[i] in shoot_people_scores:
			shoot_people_scores[shoot_peoples[i]]['scores'].append(score)
			shoot_people_scores[shoot_peoples[i]]['shoot_count'] += 1
		else:
			shoot_people_scores[shoot_peoples[i]] = {
				'scores': [score], 'shoot_count': 1
			}
	
	result = []
	for k in list(shoot_people_scores.keys()):
		if shoot_people_scores[k]['shoot_count'] < 3:
			del shoot_people_scores[k]
		else:
			# 汇总排序前三的成绩
			shoot_people_scores[k]['scores'].sort(reverse=True)
			result.append((k, sum(shoot_people_scores[k]['scores'][:3])))
	
	# 先按照总成绩逆序，在按照射击者id逆序
	result = sorted(result, key=lambda x: (-x[1], -x[0]))
	
	# 输出射击者id
	result = ','.join(map(lambda x: str(x[0]), result))
	
	print(result)
