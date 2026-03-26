#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class Fibonacci:
    '''Class for calculating Fibonacci sequence'''
    def __init__(self, N, M):
        self.N = N
        self.M = M
    def nth(self, N):
        fib = [0,1]
        for i in range(2,N):
            next_number=fib[-1]+fib[-2]
            fib.append(next_number)
        nth = fib[-1]
        return nth
    def division(self, N, M):
        fib = [0,1]
        result = []
        for i in range(2,N):
            next_number = fib[-1]+fib[-2]
            fib.append(next_number)
            if next_number%M ==0:
                result.append(next_number)
        return result

fib = Fibonacci(N= 100, M=7)
last = fib.nth(N = 100)
divide = fib.division(N=100,M=7)

print(last)
print(divide)

