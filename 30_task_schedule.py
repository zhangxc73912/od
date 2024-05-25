"""
https://zhuanlan.zhihu.com/p/639909595

1.核心定义动态规划
dp[i] = max(dp[i-1],dp[i-1]-task[i-1][1]+task[i][0]+task[i][1])
2.需要将运行时间长的任务放在最前面

1
1
2 2

2
2
1 1
2 2
3
1 1
2 2
3 3
"""


def get_use_time(task, dp):
	dp[0] = task[0][0] + task[0][1]
	for i in range(1, len(task)):
		dp[i] = max(dp[i - 1], dp[i - 1] - task[i - 1][1] + task[i][0] + task[i][1])
	print(dp[len(task) - 1])


if __name__ == '__main__':
	task_count = int(input())
	tasks = []
	for i in range(task_count):
		machine_count = int(input())
		machines = []
		for _ in range(machine_count):
			machine = list(map(int, input().split(' ')))
			machines.append(machine)
		tasks.append(machines)
	for task in tasks:
		dp = [0] * len(task)
		task.sort(key=lambda x: -x[1])  # 很重要需要将运行时间长的放在最前面
		get_use_time(task, dp)
