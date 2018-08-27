class Solution:
    def hasPath(self, s, rows, cols, path):
        # write code here
        if not s or not s[0] or not path:
            return False
        matrix=[['' for j in range(cols)] for i in range(rows)]
        count=0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j]=s[count]
                count+=1
        def dfs(matrix,i,j,s):
            if not s:
                return True
            if i<0 or i>=rows or j<0 or j>=cols:
                return False
            if matrix[i][j]!=s[0]:
                return False
            tmp=matrix[i][j]
            matrix[i][j]='#'
            res=dfs(matrix,i-1,j,s[1:]) or dfs(matrix,i+1,j,s[1:]) or dfs(matrix,i,j-1,s[1:]) or dfs(matrix,i,j+1,s[1:])
            matrix[i][j]=tmp
            return res
        for i in range(0,rows,1):
            for j in range(0,cols,1):
                if matrix[i][j]==path[0]:
                    if dfs(matrix,i,j,path):
                        return True
        return False

if __name__ == '__main__':
    s = Solution()
    matrix = "ABCESFCSADEE"
    path = "ABCB"
    rows = 3
    cols = 4
    print s.hasPath(matrix, rows, cols, path)