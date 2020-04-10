# -*- coding: utf-8 -*-
# @Time : 2020/4/10 16:20
# @Author : zdqzyx
# @File : 3.无重复字符的最长子串.py
# @Software: PyCharm

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    # dp[i]表示以i位置结尾的字符最长无重复字串长度
    if i - dp[i - 1] > d.get(s[i], -1):
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = i - d.get(s[i], -1)
    d[s[i]] = i
    return max(dp)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        #优化空间
        res = 0
        left = 0
        d = {}
        for i, c in enumerate(s):
            if c in d and d.get(c)>=left:
                left = d.get(c)+1
            d[c] = i
            res = max(res, i-left+1)
        return res

        # 典型动态规划
        n = len(s)
        if n==0:
            return 0
        dp = [1 for _ in range(n)]
        d = {s[0]:0}
        for i in range(1, n):
            if i - dp[i - 1] > d.get(s[i], -1):
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = i - d.get(s[i], -1)
            d[s[i]] = i
        return max(dp)

if __name__ == '__main__':
    s = 'abcabcbb'
    s = 'pwwkew'
    # s = 'au'
    s = 'arabcacfr'
    print(Solution().lengthOfLongestSubstring(s))