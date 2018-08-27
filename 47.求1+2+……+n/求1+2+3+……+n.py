# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.all_sum = 0

    def Sum_Solution(self, n):
        # write code here
        def getsum(n):
            self.all_sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        getsum(n)
        return self.all_sum