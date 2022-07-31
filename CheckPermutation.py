#!/usr/bin/env python
# coding: utf-8

# In[6]:


def checkPermutation(strInput1,strInput2):
    sorted_word1 = sorted(strInput1) #return ['a', 'a', 'd', 'g', 't', 'y']
    sorted_word1 = ''.join(sorted_word1) #return aadgty
    
    sorted_word2 = sorted(strInput2) 
    sorted_word2 = ''.join(sorted_word2) 
    
    if(sorted_word1==sorted_word2):
        return True
    
    return False


# In[8]:


if __name__ == "__main__":
    strInput1="god"
    strInput2="doig"
    print(checkPermutation(strInput1,strInput2))


# In[ ]:




