# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        n = n%len(s)
        if n:
            return s[n:]+s[:n]
        else:
            return s