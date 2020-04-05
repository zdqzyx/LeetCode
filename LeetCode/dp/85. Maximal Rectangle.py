# -*- coding: utf-8 -*-
# @Time : 2020/4/3 22:51
# @Author : zdqzyx
# @File : 85. Maximal Rectangle.py
# @Software: PyCharm


from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0:
            return 0
        m, n = len(matrix), len(matrix[0])

        # 动态规划
        heights  = [0 for _ in range(n)]
        lefts  = [0 for _ in range(n)]
        rights  = [n for _ in range(n)]
        max_area = 0
        for i in range(m):
            curr_left, curr_right = 0, n
            for j in range(n):
                heights[j] = heights[j]+1 if matrix[i][j]=='1' else 0
            for j in range(n):
                if matrix[i][j]=='1':
                    lefts[j] = max(lefts[j], curr_left)
                else:
                    lefts[j] = 0
                    curr_left = j+1
            for j in range(n-1, -1, -1):
                if matrix[i][j]=='1':
                    rights[j] = min(rights[j], curr_right)
                else:
                    rights[j] = n
                    curr_right = j
            for j in range(n):
                max_area = max(max_area, (rights[j]-lefts[j])*heights[j])
        return max_area


        # 暴力优化+直方图, 核心思想是遍历矩阵每个点O(MN)，遍历到第[i,j]这个点时，计算以[i,j]这个点为矩阵的右下角，最大面积是多少，其中在第i行计算第j列的宽度直方图即可求得最大矩形面积。
        max_area = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = dp[i][j-1]+1 if j>0 else 1
                width = dp[i][j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    max_area = max(max_area, width*(i-k+1))
        return max_area

        # 栈+直方图， 遍历每一行，在第i行时，dp存储了第i行为起点，每一列高度的直方图，求出这个直方图的最大值就可以得到以第i行作为起点的矩形最大面积
        dp = [0]*n
        max_area = 0
        for i in range(m):
            for j in range(n):
                dp[j] = dp[j] + 1 if matrix[i][j]=='1' else 0
            max_area = max(max_area, self.largestRectangleArea(dp))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 栈的思想
        if len(heights) == 0:
            return 0
        max_area = heights[0]
        stack = [-1, 0]
        i = 1
        while len(stack) > 1 or i < len(heights):
            if i < len(heights) and (len(stack) <= 1 or heights[stack[-1]] <= heights[i]):
                stack.append(i)
                i += 1
            else:
                t = (i - stack[-2] - 1) * heights[stack.pop()]
                max_area = max(max_area, t)
        return max_area

if __name__ == '__main__':
    s = Solution()
    mat = [
          ["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]
        ]
    # mat = [["1"]]
    mat = [["0","1"],
           ["1","0"]]
    print(s.maximalRectangle(mat))
