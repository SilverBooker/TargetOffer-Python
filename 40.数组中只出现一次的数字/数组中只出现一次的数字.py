class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here
        ans = 0
        for x in array:
            ans = ans^x
        flag = len(bin(ans)) - bin(ans).index('1')
        list1 =[]
        list2 =[]
        for x in array:
            if bin(x)[-flag] == '1':
                list1.append(x)
            else:
                list2.append(x)
        ans1 = 0;ans2=0
        for x in list1:
            ans1 = ans1^x
        for x in list2:
            ans2 = ans2^x
        return [ans1,ans2]