# -*- coding: utf-8 -*-
# @Time : 2020/4/6 14:46
# @Author : zdqzyx
# @File : 139. 单词拆分.py
# @Software: PyCharm

'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    '''
    # dp[i]表示以i位置结尾的字符串是否符合条件
    # 初始化：dp = [False for _ in range(len(s)+1)], dp[0]=True
    if dp[d] == True and s[j:i] in wordDict:
        dp[i] = True
        break
    return dp[-1]
    '''

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = dict(zip(wordDict, range(len(wordDict))))

        # 递归+回溯
        memo = [None for _ in range(len(s))]
        return self.dfs(s, wordDict, 0, memo)

        # dp[i]表示以i位置结尾的字符串是否符合条件
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s)):
            for j in range(i):
                if dp[d] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

        # 队列
        from collections import deque
        queue = deque([0])
        memo = [False for _ in range(len(s))]
        while queue:
            start = queue.popleft()
            if memo[start] == False:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        queue.append(end)
                        if end == len(s):
                            return True
                memo[start] = True
        return False

    def dfs(self, s, wordDict, start, memo):
        if start == len(s):
            return True
        if memo[start] is not None:
            return memo[start]
        for i in range(start + 1, len(s) + 1):
            if s[start:i] in wordDict and self.dfs(s, wordDict, i, memo):
                memo[start] = True
                return True
        memo[start] = False
        return False


if __name__ == '__main__':
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s, wordDict))

