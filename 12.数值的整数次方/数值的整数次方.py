# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 0
        if base == 0:
            return False
        if exponent == 0:
            return 1
        if exponent < 0:
            flag = 1
        result = 1
        for i in range(abs(exponent)):
            result *= base
        if flag == 1:
            result = 1 / result
        return result