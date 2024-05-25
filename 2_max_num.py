"""
小组中每位都有一张卡片，卡片上是6位内的正整数，将卡片连接起来可以组成多种数字，计算组成的最大数字

输入 ","号分割的多个正整数字符串，不需要考虑非数字异常情况，小组最多25个人
输出 最大数字字符串

示例：
输入：4589,101,41425,9999
输出：9999458941425101

https://leetcode.cn/problems/largest-number/description/
"""

import sys
from functools import cmp_to_key

if __name__ == '__main__':
    nums = input().split(',')

    # 按照大小排序，排序规则 x+y组成的字符串与y+x组成的字符串对比
    key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))

    # 排序
    nums = sorted(nums, key=key, reverse=True)

    # 拼接，去除全是0的场景,如果提出后为空则为0
    result = ''.join(nums).lstrip('0') or '0'

    print(result)

    