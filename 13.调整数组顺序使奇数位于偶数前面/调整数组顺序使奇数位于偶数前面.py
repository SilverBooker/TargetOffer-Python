# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for each in array:
            if(each%2==1):
                odd.append(each)
            else:
                even.append(each)
        array = odd + even
        return array

    def reOrderArray_2(self, array):
        first_even=0
        for i in range(len(array)):
            if(array[i]%3==2):
                temp = array[i]
                for j in range(i-1,first_even-1,-1):
                    array[j+1]=array[j]
                array[first_even]=temp
                first_even+=1
        return array