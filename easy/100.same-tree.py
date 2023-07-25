#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start

# 方針
# ・p,qのどちらか片方でもNoneならfalse
# ・中央のvalを比較して再帰的に解く

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p,qがともにない場合：全て比較して一致してる場合
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # p,qの親ノードが不一致
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# @lc code=end

