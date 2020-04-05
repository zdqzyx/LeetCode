# -*- coding: utf-8 -*-
# @Time : 2020/4/1 10:14
# @Author : XXX
# @Site : 
# @File : 53. Maximum Subarray.py
# @Software: PyCharm

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] + nums[i] > nums[i]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

