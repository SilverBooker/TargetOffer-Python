# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        odd = []
        even = []
        odd.append(pRoot)
        while odd or even:
            row = []
            while odd:
                tmp = odd.pop()
                row.append(tmp.val)
                if tmp.left:
                    even.append(tmp.left)
                if tmp.right:
                    even.append(tmp.right)
            if row:
                res.append(row)
            row = []
            while even:
                tmp = even.pop()
                row.append(tmp.val)
                if tmp.right:
                    odd.append(tmp.right)
                if tmp.left:
                    odd.append(tmp.left)

            if row:
                res.append(row)
        return res