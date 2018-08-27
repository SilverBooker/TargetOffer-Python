# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    '''
    最直接的做法，遍历每个结点，借助一个获取树深度的递归函数，根据该结点的左右子树高度差判断是否平衡，然后递归地对左右子树进行判断。
    '''
    def IsBalanced_Solution(self, root):
        if not root:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)
    def maxDepth(self, root):
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

class Solution2:
    '''
    这种做法有很明显的问题，在判断上层结点的时候，会多次重复遍历下层结点，增加了不必要的开销。如果改为从下往上遍历，如果子树
    是平衡二叉树，则返回子树的高度；如果发现子树不是平衡二叉树，则直接停止遍历，这样至多只对每个结点访问一次。
    '''
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.getDepth(pRoot) != -1

    def getDepth(self, root):
        if root is None:
            return 0
        left = self.getDepth(root.left)
        if left == -1:
            return -1
        right = self.getDepth(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)