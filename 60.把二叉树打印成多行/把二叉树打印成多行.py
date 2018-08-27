# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        odd = [pRoot]
        even = []
        while odd or even:
            row = []
            while odd:
                tmp = odd.pop(0)
                row.append(tmp.val)
                if not odd:
                    res.append(row)
                if tmp.left:
                    even.append(tmp.left)
                if tmp.right:
                    even.append(tmp.right)
            row = []
            while even:
                tmp = even.pop(0)
                row.append(tmp.val)
                if not even:
                    res.append(row)
                if tmp.left:
                    odd.append(tmp.left)
                if tmp.right:
                    odd.append(tmp.right)
        return res