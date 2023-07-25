#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start

# 方針
# ・与えられた値を10進数にする
# ・足し算した結果を2進数に変換する

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        bin_ans = bin(int_a + int_b)
        return bin_ans[2:]
        
# @lc code=end

print(Solution().addBinary("13", "1"))

