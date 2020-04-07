# 动态规划

## 简单
- [53.最大连续子序列和](LeetCode/dp/53.%20最大子序和.py) | [leetcode](https://leetcode-cn.com/problems/maximum-subarray/)  
    ```python
    dp[i] = max(dp[i-1]+nums[i], nums[i])  
    return max(dp)
    ```
- [198.打家劫舍](LeetCode/dp/198.%20打家劫舍.py) | [leetcode](https://leetcode-cn.com/problems/house-robber/) | 输入非负一维数组，不能连续两个数相邻，求最大和
    ```python
    dp[i] = max(dp[i-1],dp[i-2]+nums[i]) 
    return dp[-1]
    ```


## 中等
- [63.不同路径II](LeetCode/dp/63.%20不同路径II.py) | [leetcode](https://leetcode-cn.com/problems/unique-paths-ii/) | 二维数组坐上到右下，求不同路径个数  
    ```python
    if obstacleGrid[i-1][j-1] == 0:
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
    else:
        dp[i][j] = 0
    return dp[-1][-1]
    ```

- [64.最小路径和](LeetCode/dp/64.%20最小路径和.py) | [leetcode](https://leetcode-cn.com/problems/minimum-path-sum/) | 二维数组坐上到右下，求最小路径和
    ```python
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]
    ```
- [91.解码方法](LeetCode/dp/91.解码方法.py) | [leetcode](https://leetcode-cn.com/problems/decode-ways) | 一条包含字母 A-Z 的消息解码为数字的种数
    ```python
    if s[i-1]=='0':
        if s[i-2]=='1' or s[i-2]=='2':
            dp[i] = dp[i - 2]
        else:
            return 0
    elif s[i-2:i]>='10' and s[i-2:i]<='26':
        dp[i] = dp[i-1]+dp[i-2]
    else:
        dp[i] = dp[i-1]
    ```

 - [120.三角形最小路径和](LeetCode/dp/120.%20三角形最小路径和.py) | [leetcode](https://leetcode-cn.com/problems/triangle/) | 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
    ```python
    # 从下到上求 优化空间复杂度O(n)
    dp[j] = min(dp[j], dp[j+1])+triangle[i][j]
    return dp[0]
   ```
   
 - [139.单词拆分](LeetCode/dp/139.%20单词拆分.py) | [leetcode](https://leetcode-cn.com/problems/word-break/) | 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被拆分为一个或多个在字典中出现的单词。
    ```python
    # dp[i]表示以i位置结尾的字符串是否符合条件 
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for i in range(1, len(s)):
        for j in range(i):
            if dp[d] == True and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]
    ```
 - [152.乘积最大连续子数组](LeetCode/dp/152.乘积最大连续子数组.py) | [leetcode](https://leetcode-cn.com/problems/maximum-product-subarray) | 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组
    ```python
    max_val, min_val = max(nums[i], nums[i]*max_val, nums[i]*min_val), min(nums[i], nums[i]*max_val, nums[i]*min_val)
    res = max(res, max_val, min_val)
    ```

- [221.最大正方形](LeetCode/dp/221.%20最大正方形.py) | [leetcode](https://leetcode-cn.com/problems/maximal-square/) | 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
    ```python
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
    return max(dp[i][j])  
    ```
  
- [264.丑数II](LeetCode/dp/264.%20丑数%20II.py) | [leetcode](https://leetcode-cn.com/problems/ugly-number-ii) | 编写一个程序，找出第 n 个丑数。丑数就是只包含质因数 2, 3, 5 的正整数。
    ```python
    # dp[i]表示第i个丑数
    dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
    # update i2,i3,i5
    return dp[-1]
    ```
- [300.最长上升子序列](LeetCode/dp/300.最长上升子序列.py) | [leetcode](https://leetcode-cn.com/problems/longest-increasing-subsequence) | 编写一个程序，找出第 n 个丑数。丑数就是只包含质因数 2, 3, 5 的正整数。
    ```python
    # dp[i]表示以i位置结尾的最长上升子序列的长度
    if nums[i]>nums[j]:
        dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
    ```
- [338.比特位计数](LeetCode/dp/338.比特位计数.py) | [leetcode](https://leetcode-cn.com/problems/counting-bits) | 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
    ```python
    #最后有效设置位 dp[i] = dp[i&(i-1)]+1
    # 最低设置位， dp[i] = dp[i//2]+int(i%2==1)
    return dp
    ```

## 困难

- [72.编辑距离](LeetCode/dp/72.%20编辑距离.py) | [leetcode](https://leetcode-cn.com/problems/edit-distance) | 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。  
   ```python
   dp[i][j] = dp[i-1][j-1] if word1[i-1]==word2[j-1] else 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
   return dp[-1][-1]
   ```

- [85.最大矩形面积](LeetCode/dp/85.%20最大矩形面积.py) | [leetcode](https://leetcode-cn.com/problems/maximal-rectangle/) | 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。只能使用插入，删除，替换三个操作
   ```python
    if obstacleGrid[i-1][j-1] == 0:
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
    else:
        dp[i][j] = 0
    return dp[-1][-1]
   ```

