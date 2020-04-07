# -*- coding: utf-8 -*-
# @Time : 2020/4/7 22:23
# @Author : zdqzyx
# @File : 338.比特位计数.py
# @Software: PyCharm

'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
示例 1:
输入: 2
输出: [0,1,1]
示例 2:
输入: 5
输出: [0,1,1,2,1,2]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        #最后有效设置位 dp[i] = dp[i&(i-1)]+1
        dp = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            dp[i] = dp[i&(i-1)]+1
        return dp

        # 最低设置位， dp[i] = dp[i//2]+int(i%2==1)
        dp = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            dp[i] = dp[i>>1]+int(i%2==1)
        return dp

if __name__ == '__main__':
    solution = Solution()
    mat = 5
    print(solution.countBits(mat))
