# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        #建立哈希表,字符长度为8的数据类型,共有256种可能,于是创建一个长度为256的列表
        ls=[0]*256
        #遍历字符串,下标为ASCII值,值为次数
        for i in s:
            ls[ord(i)]+=1
        #遍历列表,找到出现次数为1的字符并输出位置
        for j in s:
            if ls[ord(j)]==1:
                return s.index(j)
                break
        return -1
    
class Solution2:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        stack1 = []
        stack2 = []
        for i in s:
            if i not in stack2:
                if i in stack1:
                    stack1.pop(stack1.index(i))
                    stack2.append(i)
                else:
                    stack1.append(i)
        return s.index(stack1[0])