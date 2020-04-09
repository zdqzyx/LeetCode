# -*- coding: utf-8 -*-
# @Time : 2020/4/8 21:59
# @Author : zdqzyx
# @File : 740.删除与获得点数.py
# @Software: PyCharm

'''
给定一个整数数组 nums ，你可以对它进行一些操作。
每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例 1:

输入: nums = [3, 4, 2]
输出: 6
解释:
删除 4 来获得 4 个点数，因此 3 也被删除。
之后，删除 2 来获得 2 个点数。总共获得 6 个点数。
示例 2:

输入: nums = [2, 2, 3, 3, 3, 4]
输出: 9
解释:
删除 3 来获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-and-earn
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    '''
    dp[i] = max(dp[i-1], dp[i-2]+d.get(i, 0))
    return dp[-1]
    '''
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 优化不必要的循环， 当前位置与上一个位置间隔超过1时，后面pre和cur都是cur，需要先更新下，在按照打家劫舍的解法做
        if len(nums)==0:
            return 0
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + i
        arr = sorted(d.items(), key=lambda x:x[0])
        pre, cur = 0, 0
        cur_idx = -1
        for k, v in arr:
            if k - cur_idx > 1:
                pre, cur = cur, cur
            pre, cur = cur, max(cur, pre + v)
            cur_idx = k
        return cur

        #old
        if len(nums)==0:
            return 0
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + i
        arr = sorted(d.items(), key=lambda x:x[0])
        pre, cur = (-2, 0), (-1, 0)
        for k, v in arr:
            if k - cur[0] > 1:
                pre, cur = cur, cur
            pre, cur = cur, (k, max(cur[1], pre[1] + v))
        return cur[1]

        # 转化为打家劫舍这道题的解法
        if len(nums)==0:
            return 0
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + i
        max_len = max(nums)+1
        dp = [0]*max_len
        for i in range(1, max_len):
            dp[i] = max(dp[i-1], dp[i-2]+d.get(i, 0))
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    mat = [2, 2, 3, 3, 3, 4]
    # mat = [3, 4, 2]
    # mat = [3, 1]
    mat = [8,10,4,9,1,3,5,9,4,10] # except:37
    mat = [1,6,3,3,8,4,8,10,1,3] #43
    print(solution.deleteAndEarn(mat))

