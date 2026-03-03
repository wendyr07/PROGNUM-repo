#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

#Defining the function that checks the outcome.
def check(): 
    if player == "R" or player == "P" or player == "S": #Checks for valid input.
        #Checks the status of both inputs.
        if player == "R":
            if bot == "R":
                print("It's a tie!")
            if bot == "P":
                print("You lost.")
            if bot == "S":
                print("Winner!!")
        elif player == "P":
            if bot == "P":
                print("It's a tie!")
            if bot == "S":
                print("You lost.")
            if bot == "R":
                print("Winner!!")
        elif player == "S":
            if bot == "S":
                print("It's a tie!")
            if bot == "R":
                print("You lost.")
            if bot == "P":
                print("Winner!!")
    else:
        print("No correct input is found.") #Oh oh, no valid input.
    
#Inputs.
player = input("Choose Rock, input 'R', Paper, input 'P', Siscors, input 'S': ") #Input for the player.
#Input for the bot
choice = np.array(["R", "P", "S"]) #Gives options.
bot = choice[np.random.randint(0,len(choice),1)] #Picks a random number and links it to the options.
print("The bot choose: ", bot) #Prints the bot's choice.

#Play. 
check() #Calls upon the earlier defined function.

