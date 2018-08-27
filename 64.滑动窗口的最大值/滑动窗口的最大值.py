# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        num_len = len(num)
        if size==0 or size > num_len:
            return []
        target = []
        lst = list(enumerate(num))
        d=[]
        for i in range(size):
            d.append(lst[i])
            j=i-1
            while j>-1 and d[j+1][1]>d[j][1]:
                d[j+1],d[j]=d[j],d[j+1]
                j-=1
        target.append(d[0][1])
        for j in range(size,num_len):
            print(j,num[j])
            while d and num[j] > d[-1][1]:
                d.pop()
            d.append([j,num[j]])
            while j-size>=d[0][0]:
                d.pop(0)
            target.append(d[0][1])
        return target

if __name__ == '__main__':
    s = Solution()
    num = [2,3,4,2,6,2,5,1]
    size = 3
    print(s.maxInWindows(num,size))