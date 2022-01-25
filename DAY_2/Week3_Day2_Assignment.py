#!/usr/bin/env python
# coding: utf-8

# In[2]:


#asssignment question
#python solution

def pdmax(s):
    a=int(input())
    s.append(a)
    s.pop()
    n=len(s)
    for i in range(n-1):
        if(s[i]>s[i+1]):
            maxn=s[i]
        else:
            maxn=s[i+1]
            
    print(maxn)  


# In[3]:


s=[23,43,10,67,91]
pdmax(s)


# In[ ]:




