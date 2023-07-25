#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start

# 方針
# ・numsを全探索
# ・numsがvalに一致していたら削除
# ・それ以外はnumsのk番目にその要素を加え、k+1をする

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[k] = nums[i]
                k += 1
        return k
        
# @lc code=end

