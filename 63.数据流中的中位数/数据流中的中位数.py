# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.minNums = []
        self.maxNums = []

    def Insert(self, num):
        # write code here
        if (len(self.minNums) + len(self.maxNums)) & 1 == 0:
            if len(self.maxNums) > 0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
        else:
            if len(self.minNums) > 0 and num > self.minNums[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)

    def GetMedian(self, n=None):
        # write code here
        allLen = len(self.minNums) + len(self.maxNums)
        if allLen == 0:
            return -1
        if allLen & 1 == 1:
            return self.minNums[0]
        else:
            return (self.minNums[0] + self.maxNums[0] + 0.0) / 2

    def maxHeapInsert(self, num):
        self.maxNums.append(num)
        lens = len(self.maxNums) - 1
        while lens > 0:
            if self.maxNums[lens] > self.maxNums[(lens - 1) / 2]:
                self.maxNums[lens], self.maxNums[(lens - 1) / 2] = self.maxNums[(lens - 1) / 2], self.maxNums[lens]
                lens = (lens - 1) / 2
            else:
                break

    def minHeapInsert(self, num):
        self.minNums.append(num)
        lens = len(self.minNums) - 1
        while lens > 0:
            if self.minNums[lens] < self.minNums[(lens - 1) / 2]:
                self.minNums[lens], self.minNums[(lens - 1) / 2] = self.minNums[(lens - 1) / 2], self.minNums[lens]
                lens = (lens - 1) / 2
            else:
                break

    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti] < self.maxNums[nexti + 1]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                self.maxNums[nexti], self.maxNums[i] = self.maxNums[i], self.maxNums[nexti]
                i = nexti
            else:
                break
        return t

    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[i] > self.minNums[nexti]:
                self.minNums[i], self.minNums[nexti] = self.minNums[nexti], self.minNums[i]
                i = nexti
            else:
                break
        return t