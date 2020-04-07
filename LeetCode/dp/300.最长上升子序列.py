# -*- coding: utf-8 -*-
# @Time : 2020/4/7 16:57
# @Author : zdqzyx
# @File : 300.最长上升子序列.py
# @Software: PyCharm

'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    '''
    # dp[i]表示以i位置结尾的最长上升子序列的长度
    if nums[i]>nums[j]:
        dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0

        # 贪心 + 二分查找
        tails = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]>tails[-1]:
                tails.append(nums[i])
                continue
            s, e = 0, len(tails)
            while s<e:
                m = (s+e)//2
                if tails[m]<nums[i]:
                    s = m+1
                else:
                    e = m
            tails[s] = nums[i]
        return len(tails)

        # 动态规划
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    mat = [2,3,-2,4]
    mat = [-2,0,-1]
    mat = [10,9,2,5,3,7,101,18]
    mat = [4,10,4,3,8,9]
    mat = [1,3,6,7,9,4,10,5,6]
    mat = [10,9,2,5,3,4]
    mat = [4,10,4,3,8,9]
    print(solution.lengthOfLIS(mat))