# -*- coding: utf-8 -*-
# @Time : 2020/4/6 17:12
# @Author : zdqzyx
# @File : 263. 丑数.py
# @Software: PyCharm

'''
编写一个程序判断给定的数是否为丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。
'''

class Solution:
    def isUgly(self, num: int) -> bool:
        if num<=0:
            return False
        for i in [2, 3, 5]:
            while num%i==0:
                num = num//i
        return num==1

        while num!=1:
            for i in [2, 3, 5]:
                if num%i==0:
                    num = num//i
                    break
            return False
        return True

        def recursion(num):
            if num==1:
                return True
            for i in [2, 3, 5]:
                if num % i == 0:
                    return self.isUgly(num/i)
            return False
        return recursion(num)

if __name__ == '__main__':
    solution = Solution()
    mat = 21
    print(solution.isUgly(mat))