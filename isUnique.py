#!/usr/bin/env python
# coding: utf-8

# In[34]:


def isUnique(strInput):
    #if exceeds 128 = must not unique
    if len(strInput)>128:
        return False
    
    #set array for every character to False
    char_set = [False]*128
    
    #loop array
    for char in strInput:
        
        val=ord(char) #give a value to the char
        
        if char_set[val]: #if found the char_set[a] true = appeared
            return False
        
        char_set[val]=True #set to just appeared
        
    return True


# In[33]:


if __name__ == "__main__":
    strInput="aaabbb"
    print(isUnique(strInput))


# In[ ]:




