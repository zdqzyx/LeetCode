# -*- coding: utf-8 -*-
# @Time : 2020/4/1 10:30
# @Author : zdqzyx
# @Site : 
# @File : 70. 爬楼梯.py
# @Software: PyCharm

class Solution:
    '''
    dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]
    '''
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        pre, cur = 1, 2
        for _ in range(2, n):
            pre, cur = cur, pre+cur
        return cur

if __name__ == '__main__':
    print(Solution().climbStairs(4))