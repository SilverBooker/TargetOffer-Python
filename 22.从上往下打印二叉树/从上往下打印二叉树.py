# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def PrintFromTopToBottom(self, root):
        # write code here
        l=[]
        if not root:
            return []
        q=[root]
        while len(q):
            t=q.pop(0)
            l.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return l