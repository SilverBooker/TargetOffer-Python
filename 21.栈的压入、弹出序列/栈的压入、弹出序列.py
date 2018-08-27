# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        if not pushV and not popV:
            return True
        if not pushV:
            return False
        if not popV:
            return False
        i = 0
        while pushV:
            stack.append(pushV.pop(0))
            try:
                while stack[-1] == popV[0]:
                    stack.pop()
                    popV.pop(0)
            except:
                pass
        if not stack:
            return True
        return Fals