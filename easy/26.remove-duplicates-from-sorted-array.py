#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

# 方針
# ・numsを全探索
# ・探索中の要素がそれ以前に含まれていない場合k+1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            if i not in nums[:k]: # kより前にiが含まれているか
                nums[k] = i
                k += 1
        return k
# @lc code=end

