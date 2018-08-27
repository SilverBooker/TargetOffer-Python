class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers == None:
            return 0
        count = 1
        target = numbers[0]
        if len(numbers) == 1:
            return target
        else:
            #每一个值与前一个进行比较，若不想等则-1若 相等则加1，若count=0则以当前值重新开始进行
            for i in range(1, len(numbers)):
                if count == 0:
                    target = numbers[i]
                    count = 1
                elif numbers[i] != numbers[i - 1]:
                    count -= 1
                else:
                    count += 1
        #对所得的目标值进行判定，使否为数组中出现次数超过长度一半的值，因为count=1还有可能是由于奇数个值前几个 均为不同值相消
        if count >= 1:
            times = 0
            for i in range(len(numbers)):
                if numbers[i] == target:
                    times += 1
            if times * 2 > len(numbers):
                return target
        return 0