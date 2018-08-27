# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        str2num={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        flag2num = {'-':-1,'+':1}
        first = s[0]
        if first in ['+','-']:
            flag = flag2num[first]
            x = 0
            for i in s[1:]:
                if i not in str2num:
                    return 0
                x = x*10+str2num[i]
            return flag*x
        else:
            x = 0
            for i in s:
                if i not in str2num:
                    return 0
                x=x*10+str2num[i]
            return x