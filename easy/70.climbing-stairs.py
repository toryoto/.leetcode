#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start

# 方針
# ・上り方の合計値＝１つ前までの合計値＋２つ前までの合計値
# ・→漸化式→動的計画法

class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1,2 のときは固定する
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp = [None] * (n+1) # 結果を保持する配列
            dp[1] = 1
            dp[2] = 2
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[i]

        
# @lc code=end

