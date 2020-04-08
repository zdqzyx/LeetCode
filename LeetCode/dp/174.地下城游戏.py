# -*- coding: utf-8 -*-
# @Time : 2020/4/8 0:05
# @Author : zdqzyx
# @File : 174.地下城游戏.py
# @Software: PyCharm

'''
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
为了尽快到达公主，骑士决定每次只向右或向下移动一步。

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dungeon-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import numpy as np
from typing import List
class Solution:
    '''
    #自底向上
    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
    return dp[0][0]
    '''
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[0 for i in range(m)] for _ in range(n)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in range(n-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
        for j in range(m-2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j+1]-dungeon[-1][j])

        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        return dp[0][0]

if __name__ == '__main__':
    solution = Solution()
    mat = [[-2, -3, 3],
           [-5, -10, 1],
           [10, 30, -5]]
    print(solution.calculateMinimumHP(mat))