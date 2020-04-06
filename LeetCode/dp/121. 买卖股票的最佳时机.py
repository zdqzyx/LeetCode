# -*- coding: utf-8 -*-
# @Time : 2020/4/6 13:25
# @Author : zdqzyx
# @File : 121. 买卖股票的最佳时机.py
# @Software: PyCharm


from typing import List
class Solution:
    '''
    dp[i] = max(dp[i-1], prices[i]-min_price)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        if m==0:
            return  0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, m):
            max_profit = max(max_profit, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return max_profit

        # dp
        m = len(prices)
        if m==0:
            return  0
        min_price = prices[0]
        dp = [0]*m
        for i in range(1, m):
            dp[i] = max(dp[i-1], prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return dp[-1]

        # 暴力法：
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit

if __name__ == '__main__':
    s = Solution()
    mat = [2,1,5,6,2,3]
    mat = [7,1,5,3,6,4]
    print(s.maxProfit(mat))