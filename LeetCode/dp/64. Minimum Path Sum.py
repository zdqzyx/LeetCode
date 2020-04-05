# -*- coding: utf-8 -*-
# @Time : 2020/4/2 16:44
# @Author : zdqzyx
# @File : 64. Minimum Path Sum.py
# @Software: PyCharm
'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''
from typing import List
class Solution:
    '''
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]
    '''

    def minPathSum(self, grid: List[List[int]]) -> int:
        # 压缩为一维dp
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if j==0:
                    dp[j] = dp[j] + grid[i][j]
                elif i==0:
                    dp[j] = dp[j-1] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    mat = [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
    # mat = [[0]]
    print(s.minPathSum(mat))