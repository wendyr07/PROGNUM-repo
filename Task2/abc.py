#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import *
a = float(input("a for the ax^2"))
b = float(input("b for the bx"))
c = float(input("c for the c"))

D = b**2 - 4*a*c
print("D = ", D)

if D > 0:
    x_1 = (-b + sqrt(D))/(2*a)
    x_2 = (-b - sqrt(D))/(2*a)
    print(f"There are 2 solutions: x_1 = {x_1} and x_2 = {x_2}")

elif D == 0:
    x = -b/(2*a)
    print(f"There is 1 solution: x = {x}")

else:  #D > 0
    print("There are no solutions")

