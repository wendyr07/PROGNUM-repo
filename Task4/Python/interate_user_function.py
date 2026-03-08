#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import sin, cos, exp, pi
from scipy import integrate
import numpy as np

#example func_str = "x**4+exp(sin(x)+cos(x))" 
func_str = input("Please input a function") #The string function.
xlo = 0 #Lower bound.
xhi = pi #Upper bound.

def f(x): #Defining the function needed for both monte and quad.
    return eval(func_str, {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi})  #Returning the function and the extra clause makes it safer since it doesn't have to search every python enviroment.

#Used from a session quiz.
def monte(f, a, b):
    x = np.random.uniform(a, b, 10000) #Takes points in the range given later on.
    Y = eval(f, {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi})  # evaluate f at all sampled points
    result = (b - a) * np.mean(Y)
    return result

try:
    #Quad integration:
    inte, err = integrate.quad(f, xlo, xhi) #Integrates the function and separates the tuple outcome to two variables.
    print(f"The result of the scipy.integrate.quad is: {inte}.") #Prints quad.
    print(f"The result of the Monte Carlo function is: {monte(func_str, xlo, xhi)}.") #Prints monte.
#First except clause:
except NameError: 
    print("Error: unknown function or variable used, try a different formula.") #Will appear when tan(x) is used or things like that.
#Second except clause:
except SyntaxError:
     print("Error: invalid mathematical expression, check brackets and python format.") #Will appear when the function is not written right, like missing a bracket.


# In[ ]:




