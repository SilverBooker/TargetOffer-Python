class Solution:
    def Permutation(self, ss):
        # write code here
        res = list()
        def Traversal(ss, join_ss=''):
            if ss:
                for i, s in enumerate(ss):
                    sub_ss = ss[:i] + ss[i+1:]
                    Traversal(sub_ss, join_ss+s)
            elif join_ss and join_ss not in res:
                res.append(join_ss)
        if ss:
            Traversal(ss)
        return res

class Solution_2:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss)==1:
            return [ss]
        ll = list(ss)
        str = []
        for i in range(len(ss)):
            if i > 0 and ll[i] == ll[i-1]:
                continue
            l = ll.pop(i)
            s = ''.join(ll)
            temp = self.Permutation(s)
            for j in temp:
                str.append(l+j)
            ll = list(ss)
        # str = list(set(str))
        return str

class Solution_3:
    def __init__(self):
        self.res = []
        
    def permutate(self,s,begin):
        if begin == len(s) - 1:
            self.res.append(s)
        else:
            for i in range(begin,len(s)):
                if begin != i and s[begin] == s[i]:
                    continue
                swap_s = self.swap(s,begin,i)
                self.permutate(swap_s,begin+1)
                
    def Permutation(self, ss):
        # write code here
        if len(ss) != 0:
            self.permutate(ss,0)
        return sorted(self.res)
    
    def swap(self,c, i, j):
        c = list(c)
        c[i], c[j] = c[j], c[i]
        return ''.join(c)