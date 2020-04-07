# -*- coding: utf-8 -*-
# @Time : 2020/4/7 16:37
# @Author : zdqzyx
# @File : 152.乘积最大连续子数组.py
# @Software: PyCharm

'''
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val, max_val = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            max_val, min_val = max(nums[i], nums[i]*max_val, nums[i]*min_val), min(nums[i], nums[i]*max_val, nums[i]*min_val)
            res = max(res, max_val, min_val)
        return res

if __name__ == '__main__':
    solution = Solution()
    mat = [2,3,-2,4]
    mat = [-2,0,-1]
    mat = [-4,-3,-2]
    print(solution.maxProduct(mat))
