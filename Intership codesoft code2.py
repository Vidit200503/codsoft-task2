#!/usr/bin/env python
# coding: utf-8

# In[3]:


# password-generator

import random

userinput = int(input("\nLength of password will be:- "))

smallalphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
specialsymbol = "!@#$%^&*"

ratio1 = userinput % 3
ratio2 = userinput // 3


def password(userInput):
    pass_word = ""
    for i in range(ratio1):
        pass_word += specialsymbol[random.randint(0, 7)]
        
    for i in range(ratio2):
        pass_word += alphabet[random.randint(0, 25)]
        pass_word += smallalphabet[random.randint(0, 25)]
        pass_word += numbers[random.randint(0, 9)]

    return pass_word


print(f"\nYour Password Is:- {password(userinput)}\n")


# In[ ]:




