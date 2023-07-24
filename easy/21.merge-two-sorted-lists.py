#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 返り値のリンクリストを生成
        # ans1とans2は同じオブジェクト
        # 一方が変化するともう一方も変化する（浅いコピー）
        ans1 = ans2 = ListNode(0)
        # 二つのリストの最後に達するまでループ
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ans1.next = list1
                list1 = list1.next
            else:
                ans1.next = list2
                list2 = list2.next
            ans1 = ans1.next
        ans1.next = list1 or list2
        return ans2.next
        
# @lc code=end