# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l = []
        while head != None:
            l.append(head)
            head = head.next
        if k > len(l) or k < 1:
            return
        return l[-k]

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k == 0:
            return None
        first_node = head
        # 一个辅助变量step，记录当前是第一个指针访问到正数第几个节点
        step = 0
        while first_node.next != None:
            step += 1
            if step == 1:
                first_node = head
            else:
                first_node = first_node.next

            if step == k:
                second_node = head
            elif step > k:
                second_node = second_node.next
        if step < k:
            return None
        else:
            return second_node