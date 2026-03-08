#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
from math import sqrt, pi

#Distribution variables.
A = float(input("Please put in a value for the amplitude."))
x0 = float(input("Please put in a position of the peak."))
sig = float(input("Please put in a value for the standard deviation."))
z0 = float(input("Please put in a value for the width of the peak."))

#Integration limits:
xlo = float(input("Please put in a lower integration limit."))
xhi = float(input("Please put in a higher integration limit."))

#Gauss:
def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

#Basics:
X = np.linspace(xlo -2*sig,xhi +2*sig,200) #Gets an x axis in an area based on the size of the distribution.
Y = gauss(X, A, x0, sig, z0) #Gets the Y values for the X-array above.
X_between = np.linspace(xlo, xhi, 200) #The X values for the shaded area.
Y_between = gauss(X_between, A, x0, sig, z0) #The Y values for the shaded area.

inte_gral = integrate.quad(lambda x: gauss(x, A, x0, sig, z0),xlo,xhi) #Takes the integral.
inte, err = inte_gral #Seperates the tuple into two different variables.

#Plotting the graph:
plt.plot(X,Y, label = "Distribution")
plt.fill_between(X_between, Y_between, color = "orchid", label =f"integrated area is: {inte:.2f}", alpha = 0.5) #Plots the integration part, with 2 decimals for the integration value.
plt.title("Area under a Gaussian")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.legend()
plt.show() #shows the plot.


# In[ ]:




