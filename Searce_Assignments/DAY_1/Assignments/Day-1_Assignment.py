#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Method1 : reverse an array 
def rev(lst):
    n = len(lst)
    for i in range(n-1,-1,-1):
        print(lst[i],end=" ")
        


# In[3]:


lst=[1,2,3,4,5]
rev(lst)


# In[ ]:


#Method-2 : reversing an array using 'reverse' function

def rev(lst):
    lst.reverse()
    print(lst)


# In[4]:


lst=[9,8,7,6,5]
rev(lst)


# In[ ]:




