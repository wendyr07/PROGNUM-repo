#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy as sp

def monte(f, a, b):
    x = np.random.uniform(a, b, 10000)
    Y = eval(f)  # evaluate f at all sampled points
    result = (b - a) * np.mean(Y)
    return result

f = input("Input for function")
a = float(input("lower bounds"))
b = float(input("upper bounds"))
float(monte(f, a, b))


# In[ ]:




