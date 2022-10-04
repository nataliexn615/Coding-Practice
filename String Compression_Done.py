#!/usr/bin/env python
# coding: utf-8

# String Compression: 
# 
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

# In[49]:


def compressedString(strInput):
    charLength =  len(strInput)
    outputString= ""
    count = 1
    lst = [x for x in strInput]
   
    for k in range(0,len(lst)):  
        #print(k)
        if lst[k]==lst[k-1]:
            #print(k)
            #print(k-1)
            count = count+1
        else:
            countString = str(count) 
            outputString=outputString+lst[k]+countString
            count=1
            
        
    print(outputString)


# In[50]:


if __name__ == "__main__":
    strInput="aagabccdd"
    compressedString(strInput)


# In[ ]:





# In[ ]:





# In[ ]:




