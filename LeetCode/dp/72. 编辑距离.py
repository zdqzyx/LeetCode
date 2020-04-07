# -*- coding: utf-8 -*-
# @Time : 2020/4/6 22:47
# @Author : zdqzyx
# @File : 72. 编辑距离.py
# @Software: PyCharm

'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    '''
    其中
    dp[i-1][j-1] 表示替换操作
    dp[i-1][j] 表示删除操作。为 A 的前 i - 1 个字符和 B 的前 j 个字符编辑距离的子问题。即对于 A 的第 i 个字符，我们在 B 的末尾添加了一个相同的字符，等同于删除A的第i字符
    dp[i][j-1] 表示插入操作。为 A 的
    前 i 个字符和 B 的前 j - 1 个字符编辑距离的子问题。即对于 B 的第 j 个字符，我们在 A 的末尾添加了一个相同的字符
    dp[i][j] = dp[i-1][j-1] if word1[i-1]==word2[j-1] else 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[-1][-1]
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        # 自顶向下，递归+记忆优化
        n, m = len(word1), len(word2)
        memo = [[None for j in range(m+1)] for i in range(n+1)]
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                t = len(word1) - i + len(word2) - j
                return t
            if memo[i][j] is not None:
                return memo[i][j]
            if word1[i] == word2[j]:
                t = helper(i + 1, j + 1)
                memo[i][j] = t
                return t
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                t = min(inserted, deleted, replaced) + 1
                memo[i][j] = t
                return t
        res = helper(0, 0)
        return res

        # 自顶向下， 使用系统工具帮助优化记忆
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                return min(inserted, deleted, replaced) + 1
        return helper(0, 0)

        # 自底向上， 动态规划
        n, m = len(word1), len(word2)
        dp = [[j for j in range(m+1)] for i in range(n+1)]
        # dp = [[j if i==0  else 0 for j in range(n+1)] for i in range(m+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j-1] if word1[i-1]==word2[j-1] else 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    word1 = 'horse'
    word2 = 'ros'

    # word1 = "distance"
    # word2 = "springbok"
    print(solution.minDistance(word1, word2))


