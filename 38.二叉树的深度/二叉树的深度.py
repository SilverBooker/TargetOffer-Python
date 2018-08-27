# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归写法
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot==None:return 0
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1

# 非递归版本
class Solution:
    # 层次遍历
    def levelOrder(self, root):
        # write your code here
        # 存储最后层次遍历的结果
        res = []
        # 层数
        count = 0
        # 如果根节点为空，则返回空列表
        if root is None:
            return count
        # 模拟一个队列储存节点
        q = []
        # 首先将根节点入队
        q.append(root)
        # 列表为空时，循环终止
        while len(q) != 0:
            # 使用列表存储同层节点
            tmp = []
            # 记录同层节点的个数
            length = len(q)
            for i in range(length):
                # 将同层节点依次出队
                r = q.pop(0)
                if r.left is not None:
                    # 非空左孩子入队
                    q.append(r.left)
                if r.right is not None:
                    # 非空右孩子入队
                    q.append(r.right)
                tmp.append(r.val)
            if tmp:
                count += 1  # 统计层数
            res.append(tmp)
        return count

    def TreeDepth(self, pRoot):
        # write code here
        # 使用层次遍历
        # 当树为空直接返回0
        if pRoot is None:
            return 0
        count = self.levelOrder(pRoot)
        return count