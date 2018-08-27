# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        return re.match(r'[+-]?\d*\.?\d*([eE][+-]?[0-9]+)?$',s)