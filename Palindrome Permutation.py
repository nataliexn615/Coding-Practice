#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
def checkIsPerofPa(palindromeInput):
    #isPalindrome
    char_set = [0]*128
    countMultiplesOf2 = 0
    countMultiplesOfNot2 = 0
    palindromeInput=palindromeInput.lower()
    #print(palindromeInput)
    #loop array
    for char in palindromeInput:
        #char=char.str.lower()
        val=ord(char) #give a value to the char
        char_set[val]=char_set[val]+1
        
    for x in char_set:
        if char_set[val]%2!=0: #it has multiples of 2 
            countMultiplesOfNot2=countMultiplesOfNot2+1
    
    if countMultiplesOfNot2 > 1:
        print("No") #return False
    else: print("Yes") #return True


# In[45]:


if __name__ == "__main__":
    inputStr = input("Enter String:")
    checkIsPerofPa(inputStr)


# In[ ]:




