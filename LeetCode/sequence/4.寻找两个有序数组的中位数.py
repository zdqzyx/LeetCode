# -*- coding: utf-8 -*-
# @Time : 2020/4/10 16:57
# @Author : zdqzyx
# @File : 4.寻找两个有序数组的中位数.py
# @Software: PyCharm

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2, nums1)
        s, e = 0, n1
        k = (n1 + n2 + 1) // 2
        while s<e:
            m1 = (s+e)//2
            m2 = k-m1
            if nums1[m1]<nums2[m2-1]:
                s = m1+1
            elif nums1[m1]>nums2[m2-1]:
                e = m1
            else:
                s = m1
                break
        m1 = s
        m2 = k-m1
        c1 = max(nums1[m1-1] if m1>0 else float('-inf'), nums2[m2-1] if m2>0 else float('-inf'))
        if (n1+n2)%2==1:
            return c1
        c2 = min(nums1[m1] if m1<n1 else float('inf'), nums2[m2] if m2<n2 else float('inf'))
        return (c1+c2)/2

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    nums1 = [1, 3]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
