#!/usr/bin/env python
# coding: utf-8

# In[30]:


def URLify(strInput):
    charLength =  len(strInput)
    count=0;
    for char in strInput:
        if char == " ":
            count=count+1;
    newArray = ['']*(charLength+2*count)
    k=0;
    for char in strInput:
        if char!= " ":
            newArray[k]=char;
            k=k+1;
        else:
            newArray[k]="%"
            newArray[k+1]="2"
            newArray[k+2]="0"
            k=k+3;
    returnArray = ''.join(newArray);        
    return returnArray


# In[31]:


if __name__ == "__main__":
    strInput="Mr John Smith"
    print(URLify(strInput))


# In[ ]:




