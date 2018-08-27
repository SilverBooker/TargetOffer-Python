# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res=[]
        for i in range(1,tsum//2+1):
            sumRes=i
            for j in range(i+1,tsum//2+2):
                sumRes+=j
                if sumRes==tsum:
                    res.append(list(range(i,j+1)))
                    break
                elif sumRes>tsum:
                    break
        return res

class Solution2:
    def FindContinuousSequence(self, tsum):
        # write code here
        res=[]
        low,high=1,2
        while(high>low):
            cur=(high+low)*(high-low+1)/2
            if cur==tsum:
                tmp=list()
                for i in range(low,high+1):
                    tmp.append(i)
                res.append(tmp)
                low+=1
            elif cur<tsum:
                high+=1
            else:
                low+=1
        return res