# -*- coding: utf-8 -*-
# @Time : 2020/4/2 17:15
# @Author : zdqzyx
# @File : 221. Maximal Square.py
# @Software: PyCharm

'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
'''

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m==0:
            return 0
        n = len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1]==1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                res = max(res, dp[i][j])
        return res**2

if __name__ == '__main__':
    s = Solution()
    mat = [
          [1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0]
        ]
    # mat = [
    #     [0, 1],
    #     [1, 1]
    # ]
    print(s.maximalSquare(mat))