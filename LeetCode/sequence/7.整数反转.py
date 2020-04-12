# -*- coding: utf-8 -*-
# @Time : 2020/4/11 16:42
# @Author : zdqzyx
# @File : 7.整数反转.py
# @Software: PyCharm

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def reverse(self, x: int) -> int:
        flag = int(x<0)
        x = abs(x)
        res = 0
        while x:
            res = res*10 + x%10
            x = x//10
        if res>2**31-1:
            return 0
        if flag:
            return -res
        return res


if __name__ == '__main__':
    print(Solution().reverse(120))
    print(Solution().reverse(1534236469))

