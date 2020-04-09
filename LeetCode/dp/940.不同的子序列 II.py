# -*- coding: utf-8 -*-
# @Time : 2020/4/9 0:02
# @Author : zdqzyx
# @File : 940.不同的子序列 II.py
# @Software: PyCharm

'''
给定一个字符串 S，计算 S 的不同非空子序列的个数。
因为结果可能很大，所以返回答案模 10^9 + 7.

示例 1：
输入："abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
示例 2：
输入："aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    '''
    if S[i] in char_last_idx:
        dp.append( dp[-1]*2 - dp[char_last_idx[S[i]]] )
    else:
        dp.append(dp[-1] * 2)
    char_last_idx[S[i]] = i
    return (dp[-1] - 1) % (10**9 + 7)
    '''
    def distinctSubseqII(self, S: str) -> int:
        if len(S)==0:
            return 0
        dp = [1 for _ in range(len(S)+1)]
        char_last_idx = {}
        for i in range(1, len(S)+1):
            dp[i] = dp[i-1] * 2 - (dp[char_last_idx[S[i-1]]] if S[i-1] in char_last_idx else 0)
            char_last_idx[S[i-1]] = i-1
        return (dp[-1] - 1) % (10**9 + 7)

        dp = [1]
        char_last_idx = {}
        for i in range(len(S)):
            t = dp[-1] * 2 - (dp[char_last_idx[S[i]]] if S[i] in char_last_idx else 0)
            dp.append(t)
            char_last_idx[S[i]] = i
        return (dp[-1] - 1) % (10**9 + 7)

        dp = [1]
        char_last_idx = {}
        for i in range(len(S)):
            if S[i] in char_last_idx:
                dp.append( dp[-1]*2 - dp[char_last_idx[S[i]]] )
            else:
                dp.append(dp[-1] * 2)
            char_last_idx[S[i]] = i
        return (dp[-1] - 1) % (10**9 + 7)

if __name__ == '__main__':
    solution = Solution()
    s = 'abab'
    s = 'aba' # '', 'a', 'b' 'ab', 'ba', 'aa', 'aba'
    print(solution.distinctSubseqII(s))
