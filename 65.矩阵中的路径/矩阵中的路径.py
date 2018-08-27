# -*- coding:utf-8 -*-

'''
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

class Solution:
    # rows是int，表示行数，cols表示列数
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or not path:
            return False
        # 找到与path第一个元素相等的元素的下标，然后分别从这些下标开始逐个判断
        idx = [i for i in range(len(matrix)) if matrix[i] == path[0]]
        for i in idx:
            if self.findPath(matrix, rows, cols, path, i, []):
                return True
        return False

    def findPath(self, matrix, rows, cols, path, idx, visited):
        # 如果当前下标已经访问过了，False
        if idx in visited:
            return False
        # idx索引不正确，False
        if idx < 0 or idx >= len(matrix):
            return False
        # path为空了，False
        if not path:
            return False
        # 如果前面的错误都不存在，但是当前的值，不等于path中的第一个元素，那么False
        if matrix[idx] != path[0]:
            return False
        # 如果前面的情况都不存在，也就是说当前元素与path第一个元素相等，此时如果path的长度就是为1，那么就是True
        if len(path) == 1:
            return True
        # 将当前的索引加入访问过的索引中
        visited.append(idx)
        # 判断方位：
        # 第一个元素
        if idx == 0:
            return self.findPath(matrix, rows, cols, path[1:], idx + 1, visited) or self.findPath(matrix, rows, cols,
                                                                                                  path[1:], idx + cols,
                                                                                                  visited)
        # 最后一个元素
        if idx == len(matrix) - 1:
            return self.findPath(matrix, rows, cols, path[1:], idx - 1, visited) or self.findPath(matrix, rows, cols,
                                                                                                  path[1:], idx - cols,
                                                                                                  visited)
        # 第一列
        if idx % cols == 0:
            return self.findPath(matrix, rows, cols, path[1:], idx - cols, visited) or self.findPath(matrix, rows, cols,
                                                                                                     path[1:],
                                                                                                     idx + cols,
                                                                                                     visited) \
                   or self.findPath(matrix, rows, cols, path[1:], idx + 1, visited)
        # 最后一列
        if (idx + 1) % cols == 0:
            return self.findPath(matrix, rows, cols, path[1:], idx - cols, visited) or self.findPath(matrix, rows, cols,
                                                                                                     path[1:],
                                                                                                     idx + cols,
                                                                                                     visited) \
                   or self.findPath(matrix, rows, cols, path[1:], idx - 1, visited)
        # 其他
        else:
            return self.findPath(matrix, rows, cols, path[1:], idx - cols, visited) or self.findPath(matrix, rows, cols,
                                                                                                     path[1:],
                                                                                                     idx + cols,
                                                                                                     visited) \
                   or self.findPath(matrix, rows, cols, path[1:], idx + 1, visited) or self.findPath(matrix, rows, cols,
                                                                                                     path[1:], idx - 1,
                                                                                                     visited)

if __name__ == '__main__':
    s = Solution()
    matrix = "ABCESFCSADEE"
    path = "ABCB"
    rows = 3
    cols = 4
    print s.hasPath(matrix, rows, cols, path)