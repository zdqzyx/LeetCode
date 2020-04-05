# 动态规划

## 简单
- [53.最大连续子序列和](LeetCode/dp/53.%20最大子序和.py) | [leetcode](https://leetcode-cn.com/problems/maximum-subarray/)  
    ```
    dp[i] = max(dp[i-1]+nums[i], nums[i])  
    return max(dp)
    ```
- [198.打家劫舍](LeetCode/dp/198.%20打家劫舍.py) | [leetcode](https://leetcode-cn.com/problems/house-robber/) | 输入非负一维数组，不能连续两个数相邻，求最大和
    ``` 
    dp[i] = max(dp[i-1],dp[i-2]+nums[i]) 
    return dp[-1]
    ```


## 中等
- [63.不同路径II](LeetCode/dp/63.%20不同路径II.py) | [leetcode](https://leetcode-cn.com/problems/unique-paths-ii/) | 二维数组坐上到右下，求不同路径个数  
    ```
    if obstacleGrid[i-1][j-1] == 0:
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
    else:
        dp[i][j] = 0
    return dp[-1][-1]
    ```

- [64.最小路径和](LeetCode/dp/64.%20最小路径和.py) | [leetcode](https://leetcode-cn.com/problems/minimum-path-sum/) | 二维数组坐上到右下，求最小路径和
    ``` 
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]
    ```
  
 - [120.三角形最小路径和](LeetCode/dp/120.%20三角形最小路径和.py) | [leetcode](https://leetcode-cn.com/problems/triangle/) | 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
    ``` 
    # 从下到上求 优化空间复杂度O(n)
    dp[j] = min(dp[j], dp[j+1])+triangle[i][j]
    return dp[0]
   ```
   
- [221.最大正方形](LeetCode/dp/221.%20最大正方形.py) | [leetcode](https://leetcode-cn.com/problems/maximal-square/) | 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
    ``` 
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
    return max(dp[i][j])  
    ```

## 困难

- [85.最大矩形面积](LeetCode/dp/85.%20最大矩形面积.py) | [leetcode](https://leetcode-cn.com/problems/maximal-rectangle/) | 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。  
   
   ```python
    if obstacleGrid[i-1][j-1] == 0:
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
    else:
        dp[i][j] = 0
    return dp[-1][-1]
   ```

