#!/usr/bin/env python
# coding: utf-8

# In[1]:


#traversing an array
a = [2,3,4,5,6,7]
for x in a:
    print(x,end=" ")


# In[2]:


#insertion 
a = [2,3,4,5,6,7]
a.append(7)
print(a)


# In[3]:


#inserting a an array to an array
a = [2,3,4,5,6,7]
a1 = [40,70]
a.extend(a1)
print(a)


# In[4]:


#taking user input
def af(a,n):
    
    for i in range(n):
        print(a[i])


# In[5]:


def rev_arr(A):
    
    n=len(A)
    A.reverse()
    print(A)


# In[6]:


A = [2,4,6,8,0,23]
s=rev_arr(A)


# In[7]:


A = [2,3,4,5,6]
A.reverse()
print(A)


# In[10]:


lst = [1,2,3,4,5]
n = len(lst)
for i in range(n-1,-1,-1):
    print(lst[i],end=" ")
    


# In[ ]:




