# -*- coding: utf-8 -*-
# @Time : 2020/4/2 23:30
# @Author : zdqzyx
# @File : 84. 柱状图中最大的矩形.py
# @Software: PyCharm

'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:
输入: [2,1,5,6,2,3]
输出: 10
'''

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #
        # 栈的思想
        if len(heights)==0:
            return 0
        max_area = heights[0]
        stack = [-1, 0]
        i = 1
        while len(stack)>1 or i<len(heights):
            if i<len(heights) and (len(stack)<=1 or heights[stack[-1]]<=heights[i]):
                stack.append(i)
                i += 1
            else:
                t = (i-stack[-2]-1)*heights[stack.pop()]
                max_area = max(max_area, t)
        return max_area

        # 分治的思想
        def f(heights, s, e):
            if s>e:
                return 0
            if s==e:
                return heights[s]
            idx_min, v_min = s, heights[s]
            i = s
            while i+1<=e:
                if heights[i]<v_min:
                    v_min = heights[i]
                    idx_min = i
                i+= 1
            left = f(heights, s, idx_min-1)
            right = f(heights, idx_min+1, e)
            return max(left, right, v_min*(e-s+1))
        return f(heights, 0, len(heights)-1)

        ## 循环遍历每个高度，在从当前高度出发, 左右指针找当前高度的最大宽度，得到当前高度的最大面积
        if len(heights)==0:
            return 0
        max_area = heights[0]
        for i in range(len(heights)):
            cur_width = 1
            pl = i-1
            while pl>=0 and heights[pl]>=heights[i]:
                cur_width += 1
                pl -= 1
            pr = i+1
            while pr<len(heights) and heights[pr]>=heights[i]:
                cur_width += 1
                pr += 1
            max_area = max(max_area, cur_width*heights[i])
        return max_area

        # 循环遍历每个高度，在从当前高度出发往后遍历找到最大的矩形面积
        if len(heights)==0:
            return 0
        max_area = heights[0]
        for i in range(0, len(heights)):
            min_height = heights[i]
            for j in range(i+1, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height*(j-i+1))
        return max_area

if __name__ == '__main__':
    s = Solution()
    mat = [2,1,5,6,2,3]
    mat = [6, 4, 5, 2, 4, 3, 9]
    # mat = [2,1,5,6,2,3]
    # mat = [2, 3]
    print(s.largestRectangleArea(mat))