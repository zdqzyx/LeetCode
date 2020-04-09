# -*- coding: utf-8 -*-
# @Time : 2020/4/9 15:23
# @Author : zdqzyx
# @File : 56.合并区间.py
# @Software: PyCharm

'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List

class Solution:
    '''
    按照顺序刷题
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        res = []
        intervals = sorted(intervals, key=lambda x:x[0])
        s, e = intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=e:
                e = max(e, intervals[i][1])
            else:
                res.append((s, e))
                s, e = intervals[i][0], intervals[i][1]
        res.append((s, e))
        return res

if __name__ == '__main__':
    solution = Solution()
    mat = [[1,3],[2,6],[8,10],[15,18]]
    mat = [[1,4],[4,5]]
    print(solution.merge(mat))
