# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:tin.index(root.val)+1],tin[:tin.index(root.val)])
        root.right = self.reConstructBinaryTree(pre[tin.index(root.val)+1:],tin[tin.index(root.val)+1:])
        return root