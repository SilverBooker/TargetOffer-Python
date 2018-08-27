# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return self.biSearch(data, k + 0.5) - self.biSearch(data, k - 0.5)

    def biSearch(self, data, num):
        s = 0
        e = len(data) - 1
        while s <= e:
            mid = (e - s) / 2 + s
            if data[mid] < num:
                s = mid + 1
            elif data[mid] > num:
                e = mid - 1

        return s