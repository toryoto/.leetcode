#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        tmp = 0
        roman_to_int_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        # 与えられたローマ数字を後ろから足していく
        s = s[::-1]
        for i in s:
            i = roman_to_int_dict[i] # int格納
            if tmp > i:
                sum -= i
            else:
                sum += i
            tmp = i
        return sum
# @lc code=end
print(Solution().romanToInt("MCMXCIV"))

