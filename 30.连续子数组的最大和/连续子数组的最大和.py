# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        total = 0
        maxSum= array[0]
        for i in array:
            if total>=0:
                total+=i
            else:
                total=i
            if total>maxSum:
                maxSum=total
        return maxSum

class Solution_2:
    def FindGreatestSumOfSubArray(self, array):
        res =len(array) and max(array)
        temp = 0
        for i in array:
            temp = max(i,temp+i)
            res = max(res,temp)
        return res