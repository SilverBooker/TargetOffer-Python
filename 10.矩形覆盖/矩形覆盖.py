# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = 1
        b = 2
        n = 2
        while n<number:
            n+=1
            a,b = b,a+b
        return b