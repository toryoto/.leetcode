#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start

# 方針
# １全探索：計算量n
# ２二分探索：計算量O(logn)
# →左端、右端、中央を用いて範囲を二分していく

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 # 探索範囲の左端
        right = len(nums) - 1 # 探索範囲の右端
        while left <= right:
            mid = (left + right) // 2 # 探索範囲の中央
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # targetが見つからなかった場合(どの要素よりも大きい)
        return right + 1

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     if target in nums:
    #         return nums.index(target)
    #     else:
    #         for i in range(len(nums)):
    #             if nums[i] > target:
    #                 return i
    #         return len(nums)
# @lc code=end

