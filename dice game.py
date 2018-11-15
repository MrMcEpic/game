#!/usr/bin/env python
# coding: utf-8

# In[35]:


import random
import time
import operator

class Dice():
    def __init__(self):
        self.user_num=[]
        self.track_op=str
        self.comp_ops={">":operator.gt,"<":operator.lt,"=":operator.eq} #create operator dictionary
        self.comp_roll()
        self.input_drive()
    def comp_roll(self):
        self.roll=random.randint(1,6)+random.randint(1,6) #roll 2 d6
    def input_drive(self):
        self.user_input=input("Input a number and an [in]equality to compare against 2 random d6")
        user_input=self.user_input
        print("debug: User_Input %s" % user_input)
        for i in user_input: #new way of using for... instead of i being element, i is each element of string
            print(i)
            if i.isdigit() == True:
                self.user_num.append(i) #Keep track of just number from input in list
            else:
                if i in self.comp_ops.keys(): #using dictionary keys from comp_ops to see if operator is valid
                    self.track_op = i
        self.logic()
    def logic(self):
        self.user_num=int("".join(self.user_num)) #turn number list into one int
        self.dif=self.roll-self.user_num
        self.abs_dif=abs(self.dif)
        try:
            if self.track_op in self.comp_ops:
                self.win = self.comp_ops[self.track_op](self.dif, 0)
                print("{result}\nComputer Guessed %d\nYou Guessed %d\nDifference %d".format(result="Win! :)" if self.win==True else "Lose :(") % (self.roll,self.user_num,self.abs_dif))
                time.sleep(1)
                print("Closing in 5 Seconds")
                time.sleep(5)
        except:
            print("Error: Did not input [in]equality")
            
mem=Dice()

