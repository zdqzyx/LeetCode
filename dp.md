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

- [3.无重复字符的最长子串](LeetCode/dp/3.无重复字符的最长子串.py) | [leetcode](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters) | 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    ```python
    # dp[i]表示以i位置结尾的字符最长无重复字串长度
    if i - dp[i - 1] > d.get(s[i], -1):
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = i - d.get(s[i], -1)
    d[s[i]] = i
    return max(dp)
    ```
  
- [5.最长回文子串](LeetCode/dp/5.最长回文子串.py) | [leetcode](https://leetcode-cn.com/problems/longest-palindromic-substring) | 给定一个字符串 s，找到 s 中最长的回文子串。
    ```python
    # dp[i][j]表示i开始j结尾得字符串是否为回文串
    if s[i]==s[j] and (j-i<=1 or dp[i+1][j-1]==1):
        dp[i][j] = 1
    return s[start:start+max_len]
    ```

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
- [279.完全平方数](LeetCode/dp/279.完全平方数.py) | [leetcode](https://leetcode-cn.com/problems/perfect-squares) | 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
    ```python
    # numSquares(n)=min(numSquares(n-k) + 1)∀k∈square numbers
    # dp[i]表示第i个数需要的最少平方数个数，则对于当前的第i个数来说，dp[i-k]为减去平方数k后的数字需要的最少平方数个数，在+1得到dp[i]，取所有平方数情况的最小值得到最终的dp[i]
    if i-k>=0:
        dp[i] = min(dp[i], dp[i-k]+1)
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

- [740.删除与获得点数](LeetCode/dp/740.删除与获得点数.py) | [leetcode](https://leetcode-cn.com/problems/counting-bits) | 给定一个整数数组 nums ，你可以对它进行一些操作。每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素,开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
    ```python
    dp[i] = max(dp[i-1], dp[i-2]+d.get(i, 0))
    return dp[-1]
    ```
  
- [1143.最长公共子序列](LeetCode/dp/1143.最长公共子序列.py) | [leetcode](https://leetcode-cn.com/problems/longest-common-subsequence) | 给定一个整数数组 nums ，你可以对它进行一些操作。每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素,开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
    ```python
    # 初始化 dp[n+1][m+1]
    dp[i][j] = dp[i-1][j-1]+1 if text1[i-1]==text2[j-1] else max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]
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

- [174.地下城游戏](LeetCode/dp/174.地下城游戏.py) | [leetcode](https://leetcode-cn.com/problems/dungeon-game) | 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
    ```python
    #自底向上, 倒叙逆向类型
    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
    return dp[0][0]
    ```

- [887.鸡蛋掉落](LeetCode/dp/887.鸡蛋掉落.py) | [leetcode](https://leetcode-cn.com/problems/super-egg-drop) | N层楼，K个鸡蛋，找到最小移动次数来确定F楼层，使得鸡蛋在<=F楼层时掉下不会碎，>F楼层时掉下会碎  
    $$
    dp(N, K) = 1 + \min \limits_{1<=X<=N} \{ max(dp(X-1, K-1), dp(N-X, k)) \}
    $$
    其中, dp(X-1, K-1)表示在第X层扔鸡蛋碎了，表示要到(1, X-1)层之间去找，同时K个鸡蛋减一。dp(N-X, k)表示在第X层仍鸡蛋没有碎，表示要到(N-X, N)层之间去找，同时K个鸡蛋没有消耗，不做处理
    ```python
    #自底向上
    dp[i][j] = min(dp[i][j], max(dp[x-1][j-1], dp[i-x][j]))
    return dp[-1][-1]
    ```

