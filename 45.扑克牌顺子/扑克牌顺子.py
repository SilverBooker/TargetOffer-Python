# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:return False
        a = None
        b=0
        c=0
        numbers.sort()
        for i in numbers:
            if i==0:
                b+=1
            else:
                if not a:
                    a = i
                else:
                    if a==i:
                        return False
                    else:
                        c+=i-a-1
                        a = i
        if b==c or b==4:
            return True