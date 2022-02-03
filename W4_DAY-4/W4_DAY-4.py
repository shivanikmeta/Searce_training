#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Implementing merge Sort

class Solution:
    def merge(self, A, B,C):
        
        i = 0
        j = 0
        k = 0
        while i < len(A) and j < len(B): 
            if A[i] < B[j]: 
                C[k] = A[i] 
                k = k + 1
                i = i + 1
            else: 
                C[k] = B[j] 
                k = k + 1
                j = j + 1
        while i < len(A): 
            C[k] = A[i]; 
            k = k + 1
            i = i + 1
        while j < len(B): 
            C[k] = B[j]; 
            k = k + 1
            j = j + 1
        return C
                
               
        

    def mergesort(self, Arr):
       
        if(len(Arr)<=1):
            return Arr
        
        
        #recursive case
        
        x1=Arr[:len(Arr)//2]
        x2=Arr[len(Arr)//2:]
        x1=self.mergesort(x1)
        x2=self.mergesort(x2)
        C=[0 for i in range(len(x1)+len(x2))]
        ans=self.merge(x1,x2,C)
        return ans
        


# In[ ]:




