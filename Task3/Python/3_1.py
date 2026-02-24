#!/usr/bin/env python
# coding: utf-8

# In[ ]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]


small = [] #New list for the masses smaller than the moon mass.
Mm = masses[9] #Moon mass is at index 9.

for M in masses: #Loops for the amount of values in the list.
    if M <= Mm:  #Triggers when M is smaller or the same as the moon mass.
        small.append(M) #Puts the value for M in the new list.
        
print(list(small)) #Prints the newest list.

sliced = masses[-5::1] #Slices the list to the last 5 masses.
average = sum(sliced) / len(sliced) #Takes the sum of the list above and devides is by it's length.

print(average) #Prints the average calculated above.

