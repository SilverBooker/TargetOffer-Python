class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        index = [0 for x in range(len(numbers))]
        for i in range(len(numbers)):
            if index[numbers[i]] == 0:
                index[numbers[i]] += 1
            else:
                duplication[0] = numbers[i]
                return True
        return False