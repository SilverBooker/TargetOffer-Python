# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<=0:
            return 0
        numbers = [1]
        i2,i3,i5 = 0,0,0
        for _ in range(index-1):
            n2,n3,n5 = numbers[i2]*2, numbers[i3]*3, numbers[i5]*5
            uglymin = min(n2,n3,n5)
            numbers.append(uglymin)
            i2 += (uglymin == n2)
            i3 += (uglymin == n3)
            i5 += (uglymin == n5)
        return numbers[-1]