# encoding = utf-8
class Solution:
    def printMatrix(self, matrix):
        # write code here
        result = []
        while(matrix):
            result+=matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result
    def turn(self,matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat

class Solution_2:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result
    
    def turn(self, matrix):
        # 逆时针旋转函数
        col = len(matrix[0])
        newmat = []
        for i in range(col, 0, -1):
            newmat.append([x[i-1] for x in matrix])
        return newmat
