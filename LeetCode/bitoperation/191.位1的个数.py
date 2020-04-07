# -*- coding: utf-8 -*-
# @Time : 2020/4/7 22:31
# @Author : zdqzyx
# @File : 191.位1的个数.py
# @Software: PyCharm

'''
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
示例 1：
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    任何一个数字n, n&(n-1) 都会将n二进制中最右边的1消掉
    '''
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        mask = 1
        for _ in range(32):
            if n&mask!=0:
                cnt += 1
            mask = mask<<1
        return cnt

        cnt = 0
        while n:
            n = (n-1)&n
            cnt += 1
        return cnt

if __name__ == '__main__':
    solution = Solution()
    mat = int('11111111111111111111111111111101', 2)
    print(solution.hammingWeight(mat))
