# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone(pHead.next)
        return newNode
    
class Solution_2:
    def Clone(self, head):
        nodeList = []     #存放各个节点
        randomList = []   #存放各个节点指向的random节点。没有则为None
        labelList = []    #存放各个节点的值
 
        while head:
            randomList.append(head.random)
            nodeList.append(head)
            labelList.append(head.label)
            head = head.next
        #random节点的索引，如果没有则为1   
        labelIndexList = map(lambda c: nodeList.index(c) if c else -1, randomList)
 
        dummy = RandomListNode(0)
        pre = dummy
        #节点列表，只要把这些节点的random设置好，顺序串起来就ok了。
        nodeList=map(lambda c:RandomListNode(c),labelList)
        #把每个节点的random绑定好，根据对应的index来绑定
        for i in range(len(nodeList)):
            if labelIndexList[i]!=-1:
                nodeList[i].random=nodeList[labelIndexList[i]]
        for i in nodeList:
            pre.next=i
            pre=pre.next
        return dummy.next