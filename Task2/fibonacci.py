#!/usr/bin/env python
# coding: utf-8

# In[ ]:


k = 0
n1 = 0
n2 = 1
seq = [0,1]
while k < 99:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    seq.append(n3)
    k = k + 1
print(seq[-1])

