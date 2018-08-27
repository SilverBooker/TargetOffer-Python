# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        #链表为空，或者只有一个元素，返回原列表
        if  not pHead or not pHead.next:
            return pHead
        # last为反转链表的头指针
        last = None
        while pHead:
            # 保存原链表指向第二个节点的指针
            tmp = pHead.next
            # 将头结点的的下一个指针指向反转链表
            pHead.next = last
            # 反转链表的头指针更新
            last = pHead
            # 更新原链表头指针
            pHead = tmp
        return last