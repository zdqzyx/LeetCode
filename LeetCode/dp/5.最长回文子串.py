# -*- coding: utf-8 -*-
# @Time : 2020/4/10 21:17
# @Author : zdqzyx
# @File : 5.最长回文子串.py
# @Software: PyCharm

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    # dp[i][j]表示i开始j结尾得字符串是否为回文串
    if s[i]==s[j] and (j-i<=1 or dp[i+1][j-1]==1):
        dp[i][j] = 1
    return s[start:start+max_len]
    '''
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        max_len = 1
        start = 0
        for j in range(1, n):
            for i in range(j+1):
                if s[i]==s[j] and (j-i<=1 or dp[i+1][j-1]==1):
                    dp[i][j] = 1
                    if j-i+1>max_len:
                        max_len = j-i+1
                        start = i
        return s[start:start+max_len]
        
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        max_len = 0
        start = 0
        for _len in range(n):
            for i in range(n-_len):
                j = i+_len
                if s[i]==s[j] and (j-i<=1 or dp[i+1][j-1]==1):
                    dp[i][j] = 1
                    if j-i+1>max_len:
                        max_len = j-i+1
                        start = i
        return s[start:start+max_len]


if __name__ == '__main__':
    s = 'abcabcbb'
    s = 'babad'
    s = 'babab'
    # s = "cbbd"
    # s = 'a'
    print(Solution().longestPalindrome(s))