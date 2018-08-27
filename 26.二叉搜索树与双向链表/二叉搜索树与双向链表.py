# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        
        # 连接根与左子树最大结点
        if left:
            while (left.right):
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree
        
        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        
        # 连接根与右子树最小结点
        if right:
            while (right.left):
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree
        
        while (pRootOfTree.left):
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

class Solution_2:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:return
        self.arr = []
        self.midTraversal(pRootOfTree)
        for i,v in enumerate(self.arr[:-1]):
            v.right = self.arr[i + 1]
            self.arr[i + 1].left = v
        return self.arr[0]
 
    def midTraversal(self, root):
        if not root: return
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)