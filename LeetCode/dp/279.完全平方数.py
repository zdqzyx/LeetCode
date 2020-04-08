# -*- coding: utf-8 -*-
# @Time : 2020/4/8 14:38
# @Author : zdqzyx
# @File : 279.完全平方数.py
# @Software: PyCharm

'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
示例 1:
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    # numSquares(n)=min(numSquares(n-k) + 1)∀k∈square numbers
    # dp[i]表示第i个数需要的最少平方数个数，则对于当前的第i个数来说，dp[i-k]为减去平方数k后的数字需要的最少平方数个数，在+1得到dp[i]，取所有平方数情况的最小值得到最终的dp[i]
    if i-k>=0:
        dp[i] = min(dp[i], dp[i-k]+1)
    return dp[-1]
    '''
    def numSquares(self, n: int) -> int:
        import math
        dp = [float('inf') for _  in range(n+1)]
        dp[0] = 0
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        for i in range(1, n+1):
            for k in squares:
                if i-k>=0:
                    dp[i] = min(dp[i], dp[i-k]+1)
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    mat = 13
    print(solution.numSquares(mat))

