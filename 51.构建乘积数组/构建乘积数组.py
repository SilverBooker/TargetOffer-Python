class Solution:
    def multiply(self, A):
        B = []
        for i in range(0,len(A)):
            b = 1
            for j in range(0,len(A)):
                if j != i:
                    b *= A[j]
            B.append(b)
        return B

class Solution2:
    def multiply(self, A):
        if A == None or len(A) <= 0:
            return
        length = len(A)
        aList = [1] * length
        for i in range(1, length):
            aList[i] = aList[i-1] * A[i-1]
        temp = 1
        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            aList[i] *= temp
        return aList