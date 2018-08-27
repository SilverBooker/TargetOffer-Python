# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        blank_sum = len(filter(lambda x: x == ' ', s))
        if blank_sum == 0 and len(s) < 1:
            return s

        # 拓展字符串数组长度
        string = list(s)
        newLength = len(string) + blank_sum * 2
        string.extend([' '] * blank_sum * 2)

        p2 = newLength - 1
        p1 = p2 - blank_sum * 2

        while p1 != p2:
            if string[p1] == ' ':
                string[p2] = '0'
                string[p2 - 1] = '2'
                string[p2 - 2] = '%'
                p2 -= 3
                p1 -= 1
            else:
                string[p2] = string[p1]
                p1 -= 1
                p2 -= 1

        return ''.join(string)