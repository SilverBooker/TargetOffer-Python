# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        a = 0
        if n >= 0:
            for i in bin(n):
                if i == '1':
                    a += 1
            return a
        if n < 0:
            n = -n-1
            for i in bin(n):
                if i == '1':
                    a += 1
            return 32-a