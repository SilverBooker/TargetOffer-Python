# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def sym_Tree(self, root1, root2):
        """判断两个树是不是对称的

        :param root1:
        :param root2:
        :return:
        """
        # 匹配完毕
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        if root2 and not root1:
            return False
        # 两个树不为空树
        if root2.val != root1.val:
            return False
        # 判断左右子树是否一致
        left = self.sym_Tree(root1.left, root2.right)
        # 采用熔断算法
        if not left:
            return False
        right = self.sym_Tree(root1.right, root2.left)
        if not right:
            return False
        return True

    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        result = self.sym_Tree(pRoot, pRoot)
        return result