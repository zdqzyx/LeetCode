# -*- coding: utf-8 -*-
# @Time : 2020/4/11 11:11
# @Author : zdqzyx
# @File : 6.Z 字形变换.py
# @Software: PyCharm

'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import numpy as np
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        res = ['' for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)

        n =len(s)
        res = ['' for _ in range(numRows)]
        i, flag = 0, 1
        for c in s:
            res[i] += c
            if flag==1 and i<numRows:
                i+=1
            if i==numRows:
                i = numRows-1
                flag = 0
            if i==0:
                i=1
                flag = 1
            if flag==0 and i>=0:
                i-=1
        return ''.join(res)

        cols = n//(2*numRows-2)*(numRows-1)+n%(2*numRows-2)//numRows+n%(2*numRows-2)%numRows
        arr = [['' for _ in range(cols)] for _ in range(numRows)]
        cnt = 0
        j = 0
        while cnt<n:
            i=0
            while cnt<n and i<numRows:
                arr[i][j] = s[cnt]
                i+=1
                cnt+=1
            i=numRows-2
            j+=1
            while cnt<n and i>0:
                arr[i][j] = s[cnt]
                i-=1
                j+=1
                cnt+=1
        # print(np.array(arr))
        return ''.join([''.join(item) for item in arr])

if __name__ == '__main__':
    print(Solution().convert('LEETCODEISHIRING', 4)) # LDREOEIIECIHNTSG
    print(Solution().convert('sdf', 1))