# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        #1的个数
        count=0
        #i当前位
        i=1
        current=0
        after=0
        before=0
        while((n/i)!=0):
            #当前位数字
            current=(n/i)%10
            #高位数字
            before=n/(i*10)
            #低位数字
            after=n-(n/i)*i
            #如果为0,出现1的次数由高位决定,等于高位数字 * 当前位数
            if current==0:
                count+=before*i
            #如果为1,出现1的次数由高位和低位决定,高位*当前位+低位+1
            elif current==1:
                count+=before*i+after+1
            #如果大于1,出现1的次数由高位决定,//（高位数字+1）* 当前位数
            else:
                count+=(before+1)*i
            i=i*10
        return count