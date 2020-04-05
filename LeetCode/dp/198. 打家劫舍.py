# -*- coding: utf-8 -*-
# @Time : 2020/4/1 11:01
# @Author : zdqzyx
# @File : 198. 打家劫舍.py
# @Software: PyCharm

'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12
'''

from typing import List
class Solution:
    '''
    dp[i] = max(dp[i-1],dp[i-2]+nums[i]) , num[i]为当前房屋的金额
    return dp[-1]
    '''
    def rob(self, nums: List[int]) -> int:
        # 优化空间复杂度为O（1），时间复杂度O（n）
        pre, cur = 0, 0
        for num in nums:
            pre, cur = cur, max(pre+num, cur)
        return cur

        # 容易理解的状态转移方程: dp[i] = max(dp[i-1],dp[i-2]+nums[i]) , num[i]为当前房屋的金额
        n = len(nums)
        dp = [0]*(n+2)
        for i in range(2,n+2):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-2])
        return dp[-1]

if __name__ == '__main__':
    print(Solution().rob([2,7,9,3,1]))