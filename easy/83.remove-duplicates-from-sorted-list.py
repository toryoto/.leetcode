#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next == None:
                return head
            current = head.next
            prev = head
            while current != None:
                if current.val == prev.val:
                    prev.next = current.next
                else:
                    prev = current
                current = current.next
            return head
        return head
# @lc code=end

