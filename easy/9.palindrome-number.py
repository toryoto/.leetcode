#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
# @lc code=end

print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(442424))