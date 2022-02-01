#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sorting an array using Bubble Sort

class Solution:
    def bubbleSort(self, Arr):
        # write your method here
        n=len(Arr)
        for i in range(n):
            for j in range(n-i-1):
                if(Arr[j]>Arr[j+1]):
                    temp=Arr[j]
                    Arr[j]=Arr[j+1]
                    Arr[j+1]=temp
                    
        return Arr


# In[2]:


# Imlementing Selection Sort

class Solution:
    def selectionSort(self, A):
        # write your method here
        n=len(A)
        for i in range(n):
            start=i
            for j in range(i+1,n):
                if(A[start]>A[j]):
                    start=j
                    
            A[i],A[start]=A[start],A[i]
        
        return A    


# In[ ]:




