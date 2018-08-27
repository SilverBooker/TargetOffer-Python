# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        # write code here
        mergeHead = ListNode(90)
        p = mergeHead
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                mergeHead.next = pHead2
                pHead2 = pHead2.next
            else:
                mergeHead.next = pHead1
                pHead1 = pHead1.next

            mergeHead = mergeHead.next
        if pHead1:
            mergeHead.next = pHead1
        elif pHead2:
            mergeHead.next = pHead2
        return p.next

class Solution_2:
    # 递归版本
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        pHead = ListNode(0)
        if pHead1.val < pHead2.val:
            pHead = pHead1
            pHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pHead = pHead2
            pHead.next = self.Merge(pHead1, pHead2.next)
        return pHead