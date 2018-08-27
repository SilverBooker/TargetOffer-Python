# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow, fast=pHead,pHead
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                slow2=pHead
                while slow!=slow2:
                    slow=slow.next
                    slow2=slow2.next
                return slow