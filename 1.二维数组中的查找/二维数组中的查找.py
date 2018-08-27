# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        rows = len(array)
        columns = len(array[0])
        if columns == 0:
            return False
        row = 0
        column = columns - 1
        while row < rows and column >= 0:  # 没有走到尽头
            if array[row][column] == target:  # 相等
                return True
            elif array[row][column] > target:
                column -= 1
            else:
                row += 1
        return False