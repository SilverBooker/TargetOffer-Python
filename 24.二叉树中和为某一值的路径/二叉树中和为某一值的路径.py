# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def FindPath(self,root,expectNumber):
        if not root or not expectNumber:
            return []
        if not root.left and not root.right:
            return [[root.val]] if root.val==expectNumber else []
        left=self.FindPath(root.left,expectNumber-root.val)
        right=self.FindPath(root.right,expectNumber-root.val)
        return [[root.val]+i for i in left+right]