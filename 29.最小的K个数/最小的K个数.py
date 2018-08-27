# -*- coding:utf-8 -*-
class Solution_1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or len(tinput) < k:
            return []
         
        return [x for x in self.get_smallest_k(tinput, k)]
         
    def heapify(self, nums, start, end):
        left, right = start*2 + 1, start*2 + 2
         
        smallest = left if left <= end and nums[left] < nums[start] else start
        smallest = right if right <= end and nums[right] < nums[smallest] else smallest
         
        if smallest != start:
            nums[smallest], nums[start] = nums[start], nums[smallest]
            self.heapify(nums, smallest, end)
     
    def build_heap(self, nums):
        for i in range(len(nums)//2 - 1, -1, -1):
            self.heapify(nums, i, len(nums) - 1)
             
    def get_smallest_k(self, nums, k):
        self.build_heap(nums)
        res = []
        for i in range(len(nums) - 1, len(nums) - 1 - k, - 1):
            nums[i], nums[0] = nums[0], nums[i]
            yield nums[i]
            self.heapify(nums, 0, i - 1)

import random
class Solution_2:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        n = len(tinput)
        if n<=0 or k>n:
            return []
        if k==0:
            return []
        start = 0
        end = n-1
        index = self.partition(tinput,start,end)
        while index != k-1:
            if index >k-1:
                end = index - 1
                index = self.partition(tinput,start,end)
            else:
                start = index +1
                index = self.partition(tinput,start,end)
        res = tinput[:k]
        res=sorted(res)
        return res
 
    def partition(self,arr,start,end):
        if start==end:
            p=start
        else:
            p = random.randrange(start,end)
        arr[p],arr[end]=arr[end],arr[p]
        small = start-1
        for i in range(start,end):
            if arr[i]<arr[end]:
                small+=1
                if small != i:
                    arr[small],arr[i]=arr[i],arr[small]
        small +=1
        arr[small],arr[end]=arr[end],arr[small]
        return small
    
class Solution_3:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k>len(tinput):
            return []
        n=len(tinput)-1
        def quickfind(left,right,k):
            if(left>=right):
                return
            else:
                i=left-1
                j=left
                var=tinput[right]
                while(j<right):
                    if tinput[j]<var:
                        i+=1
                        tinput[i],tinput[j]=tinput[j],tinput[i]
                    j+=1
                tinput[i+1],tinput[right]=tinput[j],tinput[i+1]
                if(i+1-left+1==k):
                    return
                elif (i+1-left+1<k):
                    quickfind(i+2,right,k-(i+1-left+1))
                else:
                    quickfind(left,i,k)
        quickfind(0,n,k)
        return sorted(tinput[:k])

if __name__ == '__main__':
    s=Solution_3()
    a = [4, 5, 1, 6, 2, 7, 3, 8]
    print(s.GetLeastNumbers_Solution(a,4))