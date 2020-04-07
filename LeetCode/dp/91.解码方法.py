# -*- coding: utf-8 -*-
# @Time : 2020/4/7 15:12
# @Author : zdqzyx
# @File : 91.解码方法.py
# @Software: PyCharm

'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        ppre, pre = 1, int(s[0]!='0')
        for i in range(1, len(s)):
            ppre, pre = pre, ppre*int(10<= int(s[i-1:i+1]) <= 26) + pre*int(int(s[i])>0)
        return pre

        n = len(s)
        if n==0:
            return 0
        if s[0]=='0':
            return 0
        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            if s[i-1]=='0':
                if s[i-2]=='1' or s[i-2]=='2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i-2:i]>='10' and s[i-2:i]<='26':
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    s = '226'
    s = '12'
    print(solution.numDecodings(s))
