#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        prefix = ""
        # 最も短い文字列以上は探索する必要がない
        for i in range(len(strs[0])):
            for s in strs:
                # これ以上探索できない場合は現在の値を返す
                if (i == len(s)) or (s[i] != strs[0][i]):
                    return prefix
            # 探索しているすべての文字が一致した場合
            prefix += strs[0][i]
        return prefix


print(Solution().longestCommonPrefix(["fag","facecar","car"]))
        
# @lc code=end

