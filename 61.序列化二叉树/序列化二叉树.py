# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    flag = -1
    #序列化：将一个二叉树的节点值转化为字符，并且在每次二叉树的结点不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
    #反序列化：使用字符串中的字符创建一个二叉树
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        #层次遍历二叉树，不存在的节点即为'#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    def Deserialize(self, s):
        # write code here
        #将层次遍历的得到的序列还原成原来的二叉树
        #使用一个全局变量flag来记录节点的移动
        array =s.split(',')
        self.flag += 1
        if self.flag >= len(array):
            return None
        root = None
        if array[self.flag] != '#':
            #第一次递归
            #此时flag为0，记录的是第一个节点，每个节点的类型均为字符串类型，需要转换为数值类型
            root = TreeNode(int(array[self.flag]))
            #此时flag为1，记录的是第二个节点
            root.left = self.Deserialize(s)
            #此时flag为2，记录的是三个节点
            root.right = self.Deserialize(s)
        return root