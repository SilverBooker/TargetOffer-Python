# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        num1 = 0
        num2 = 0
        p1 = pHead1
        p2 = pHead2
        while p1:
            num1 += 1
            p1 = p1.next
        while p2:
            num2 += 1
            p2 = p2.next
        if num1 >= num2:
            n = num1 - num2
            while n > 0:
                n -= 1
                pHead1 = pHead1.next
        else:
            n = num2 - num1
            while n > 0:
                n -= 1
                pHead2 = pHead2.next
        while pHead1:
            if pHead1 == pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None