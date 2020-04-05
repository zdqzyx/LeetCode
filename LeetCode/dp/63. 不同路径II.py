# -*- coding: utf-8 -*-
# @Time : 2020/4/2 12:46
# @Author : zdqzyx
# @File : 63. 不同路径II.py
# @Software: PyCharm

'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
'''

from typing import List
class Solution:
    '''
    dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]
    '''
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # 定义状态：即数据元素的含义：dp表示当前位置的路径条数
        # 建立状态转移方程：dp[i] = dp[i]+dp[i-1]
        # 设定初始值：增加初始值1，即dp = [0]*(n+1)
        # 状态压缩：即优化数组空间,将二维数组压缩到一维数组,逐行计算当前最新路径条数，并覆盖上一行对应的路径条数
        # 选取dp[-1]表示到达finish位置路径总条数
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0]*(n+1)
        if n>=1:
            dp[1] = 1
        for i in range(0, m):
            for j in range(1, n+1):
                dp[j] = 0 if obstacleGrid[i][j-1] else dp[j] + dp[j - 1]
            dp[0] = 0
        return dp[-1]

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[1 if (i==0 or j==0) and obstacleGrid[i-1][j-1]!=1 else 0 for j in range(n+1) ] for i in range(m+1)]
        dp = [[ 0 for j in range(n+1) ] for i in range(m+1)]
        if obstacleGrid[0][0]==0:
            dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    mat = [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
    # mat = [[0]]
    print(s.uniquePathsWithObstacles(mat))