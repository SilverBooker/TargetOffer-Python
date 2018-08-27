# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = map(str,numbers)
        numbers.sort(cmp = lambda x,y : int(x+y)-int(y+x))
        return ''.join(numbers)