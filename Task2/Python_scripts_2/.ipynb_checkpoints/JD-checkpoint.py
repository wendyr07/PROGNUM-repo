#!/usr/bin/env python
# coding: utf-8

# In[ ]:


y = input("Do you want the difference between 2 dates, yes or no? ") #Choose whether you'd like to calculate one date or two dates.

D1 = float(input("Day: ")) #Fill in the first day, float so you can fill in decimal numbers.
M1 = int(input("Month: ")) #Fill in the first month.
Y1 = int(input("Year: "))  #Fill in the first year.

#Formula for the first date.
JD_1 = 367*Y1-7*(Y1+(M1+9)/12)/4-3*((Y1+(M1-9)/7)/100+1)/4+(275*M1)/9+D1+1721029-0.5
print(f"The first date as a Julian date is: {int(JD_1)} days.") #Printed as integer to keep the answer shorter.

#extension
if y == "yes": #If you put "yes" as the first one, you get a second date to fill.
    D2 = float(input("Day 2: ")) #Fill in the second day, float so you can fill in decimal numbers.
    M2 = int(input("Month 2: ")) #Fill in the second month.
    Y2 = int(input("Year 2: "))  #Fill in the second year.
    
    #Formula for the second date.
    JD_2 = 367*Y2-7*(Y2+(M2+9)/12)/4-3*((Y2+(M2-9)/7)/100+1)/4+(275*M2)/9+D2+1721029-0.5
    print(f"The second date as a Julian date is: {int(JD_2)} days.") #Printed as integer to keep the answer shorter.

    #Difference of the dates.
    JD_difference = abs(JD_2 - JD_1) #Takes the absolute of the equation, because of the possibility that the dates were filled in wrongly.
    print(f"The difference between the two dates in Julian date form is: {int(JD_difference)} days.") #Prints as an integer to keep the answer reasonably short (no decimals).

