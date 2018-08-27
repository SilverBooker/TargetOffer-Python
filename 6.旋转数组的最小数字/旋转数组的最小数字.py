#coding=utf-8
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        high=len(rotateArray)-1
        if high==-1:
            return 0
        low=0
        while low<=high:
            mid=(high+low)//2
            if rotateArray[mid]<rotateArray[high]:
                if rotateArray[mid]<rotateArray[mid-1]:
                    return rotateArray[mid]
                high=mid-1
            elif rotateArray[mid]>rotateArray[high]:
                low=mid+1
            else:
                return rotateArray[mid]
        return rotateArray[low]