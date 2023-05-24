#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

# 全探索
class Solution:
    # numは要素がint型のリスト、targetはint型、返り値は要素がint型のリスト
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
# @lc code=end

