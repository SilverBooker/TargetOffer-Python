# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        a = b = c = 0
        x = float('inf')
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if tsum==array[i]+array[j]:
                    c = 1
                    if array[i]*array[j]<x:
                        x = array[i]*array[j]
                        a,b = array[i],array[j]
        if c:
            return [a,b]
        else:
            return []

class Solution2:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array)==0 or array[-1]*2<tsum or array[0]>tsum:
            return []
        res = []
        n = len(array)
        i,j=0,n-1
        while(i<j):
            if array[i]+array[j]==tsum:
                res.append(array[i])
                res.append(array[j])
                break
            while (i<j and array[i]+array[j]>tsum):
                j-=1
            while (i<j and array[i]+array[j]<tsum):
                i+=1
        return res