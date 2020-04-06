# -*- coding: utf-8 -*-
# @Time : 2020/4/6 17:44
# @Author : zdqzyx
# @File : 264. 丑数 II.py
# @Software: PyCharm

'''
编写一个程序，找出第 n 个丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。
示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    # dp[i]表示第i个丑数
    dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
    update i2,i3,i5
    return dp[-1]
    '''
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        # 三指针初始化
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            # 找出制造当前这个最小值的指针，然后前移一位
            if dp[i2] * 2 == dp[i]:
                i2 += 1
            if dp[i3] * 3 == dp[i]:
                i3 += 1
            if dp[i5] * 5 == dp[i]:
                i5 += 1
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    mat = 10
    print(solution.nthUglyNumber(mat))



