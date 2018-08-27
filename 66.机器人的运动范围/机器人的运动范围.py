# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, k, m, n):
        def fsum(n):
            return sum(map(int,str(n)))
        matrix = []
        for i in range(m):
            for j in range(n):
                matrix.append(fsum(i) + fsum(j))
        visited = set()
        count = [0]
        def dfs(i,j):
            visited.add((i,j))
            count[0] += 1
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if -1 < x < m and -1 < y < n and (x,y) not in visited:
                    if matrix[x*n + y] <= k:
                        dfs(x,y)
        if matrix[0] <= k:
            dfs(0,0)
        return count[0]

if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(18,35,37))