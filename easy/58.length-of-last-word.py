#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start

# 方針
# ・各文字をスペースで区切る
# ・最後の文字の長さを返す

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 文字列の長さゼロの場合
        if len(s) == 0:
            return 0
        s_list = s.split()
        return len(s_list[-1])
        
# @lc code=end
print(Solution().lengthOfLastWord("fly me   to   the moon  "))
