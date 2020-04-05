# -*- coding: utf-8 -*-
# @Time : 2020/4/1 10:14
# @Author : XXX
# @Site : 
# @File : 53. 最大连续子序和.py
# @Software: PyCharm

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

from typing import List
class Solution:
    '''
    dp[i] = max(dp[i-1]+nums[i], nums[i])
    return max(dp)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

