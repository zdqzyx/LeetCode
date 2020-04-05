# -*- coding: utf-8 -*-
# @Time : 2020/4/1 11:40
# @Author : zdqzyx
# @File : 120. 三角形最小路径和.py
# @Software: PyCharm

'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）
'''

from typing import List
class Solution:
    '''
    ref:https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-de-jie-jue-ban-f/
    求三角形最短路径和
    # 从下到上求 优化空间复杂度O(n)
    dp[j] = min(dp[j], dp[j+1])+triangle[i][j]
    return dp[0]

    # 从下到上求
    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])+dp[i][j]
    return dp[0][0]

    # 从上到下求
    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
    return min(dp[-1])
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 从下到上求 优化空间复杂度O(n)
        rows = len(triangle)
        dp = triangle[-1]
        for i in reversed(range(rows-1)):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1])+triangle[i][j]
        return dp[0]

        # 从下到上求
        rows = len(triangle)
        dp = triangle
        for i in range(rows-2, -1, -1):
            for j in range(i, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])+dp[i][j]
        return dp[0][0]

        # 从下到上求
        rows = len(triangle)
        dp = [[0]*i for i in range(1, rows+1)]
        dp[-1] = triangle[-1]
        for i in range(rows-2, -1, -1):
            for j in range(i, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])+triangle[i][j]
        return dp[0][0]

        # 从上到下求
        rows = len(triangle)
        dp = [[0]*i for i in range(1, rows+1)]
        dp[0][0] = triangle[0][0]
        dp[0][-1] = triangle[0][-1]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0]+triangle[i][0]
            dp[i][-1] = dp[i-1][-1]+triangle[i][-1]

        for i in range(1, rows):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
        return min(dp[-1])

if __name__ == '__main__':
    arr = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(Solution().minimumTotal(arr))