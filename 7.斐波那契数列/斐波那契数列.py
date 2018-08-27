from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
class Solution:
    @memo
    def Fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        i,a,b=0,0,1
        if n == 0:
            return a
        while i < n-1:
            a,b = b,a+b
            i = i + 1
        return b