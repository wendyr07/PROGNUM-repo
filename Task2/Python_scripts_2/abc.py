#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import *
a = float(input("a for the ax^2: ")) #Float input for the a, since there could be decimals or negative numbers.An example: 1.
b = float(input("b for the bx: "))   #" ". An example: -9.
c = float(input("c for the c: "))    #" ". An example: 14.

D = b**2 - 4*a*c  #Calculates the discriminant.
print("The discriminant is: ", D)  #Prints the discriminant.

if D > 0:  #If D>0 there should be two solutions, so then calculate 2 solutions.
    x_1 = (-b + sqrt(D))/(2*a)  #Calculation solution 1
    x_2 = (-b - sqrt(D))/(2*a)  #Calculation solution 2
    print(f"There are 2 solutions: x_1 = {x_1} and x_2 = {x_2}")  #Prints the 2 solutions with an f string.
    #Example solutions: x_1 = 7.0 and x_2 = 2.0

elif D == 0:  #If D is not positive, but D is 0, there is 1 solution.
    x = (-b/(2*a))  #Said solution
    print(f"There is 1 solution: x = {x}") #Prints the solution

else:  #If D is neither positive nor 0, the value should be negative and there are no solutions.
    print(f"There are no solutions") #Prints the outcome of an negative discriminant (no solutions).

