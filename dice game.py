#!/usr/bin/env python
# coding: utf-8

# In[1]:


# %load "dice game.py"
#!/usr/bin/env python

# In[6]:

#test
import random
import time

class Dice():
    def __init__(self):
        self.user_num=[]
        self.track_op=str
        self.comp_roll()
        self.input_drive()
    def comp_roll(self):
        self.roll=random.randint(1,6)+random.randint(1,6) #roll 2 d6
    def input_drive(self):
        self.user_input=input("Guess? 2-12 > | < | =\n")
        user_input=self.user_input
        #user_input=list(user_input)
        print("debug: User_Input %s" % user_input)
        for i in range(len(user_input)):
            if user_input[i].isdigit() == True:
                self.user_num.append(user_input[i]) #Keep track of just number from input in list
                print("debug:",user_input[i],"is number")
            else:
                #print(user_input[i],"is not number")
                if user_input[i] == ">":
                    self.track_op=">"
                    print(self.track_op)
                elif user_input[i] == "<":
                    self.track_op="<"
                    print(self.track_op)
                elif user_input[i] == "=":
                    self.track_op="="
                    print(self.track_op)
        self.user_num=int("".join(self.user_num)) #turn number list into one int
        print("debug: user_num is %s" % self.user_num)
        print("debug: roll %s" % self.roll)
        self.logic()
    def logic(self):
        dif=self.roll-self.user_num
        abs_dif=abs(dif)
        #end={"won":"Win!","lost":"Lost"}
        if self.track_op == ">":
            if dif > 0:
                win=True
                #win_lose="won"
            else:
                win=False
                #win_lose="lost"
        elif self.track_op == "<":
            if dif < 0:
                win=True
                #win_lose="won"
            else:
                win=False
                #win_lose="lost"
        elif self.track_op == "=":
            if dif == 0:
                win=True
                #win_lose="won"
            else:
                win=False
                #win_lose="lost"
        print("{win}\nComputer Guessed %d\nYou Guessed %d\nDifference %d\nClossing in 5 Seconds".format(win="Win! :)" if win==True else "Lose :(") % (self.roll,self.user_num,abs_dif))
        #print("%s\nComputer Guessed %s\nYou Guessed %s\nDifference %s" % (end[win_lose],self.roll,self.user_num,abs_dif))
        time.sleep(5)
mem=Dice()


# In[ ]:


## 


# In[ ]:




