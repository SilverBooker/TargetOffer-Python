# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.res = []
        self.dfs(pRoot)
        return self.res[k - 1] if 0 < k <= len(self.res) else None

    def dfs(self, pRoot):
        if not pRoot:
            return
        self.dfs(pRoot.left)
        self.res.append(pRoot)
        self.dfs(pRoot.right)