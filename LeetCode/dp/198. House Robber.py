# -*- coding: utf-8 -*-
# @Time : 2020/4/1 11:01
# @Author : zdqzyx
# @File : 198. House Robber.py
# @Software: PyCharm

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