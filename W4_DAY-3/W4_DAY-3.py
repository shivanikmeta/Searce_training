#!/usr/bin/env python
# coding: utf-8

# In[1]:


#merging 2 arrays
class Solution:
    def mergeTwoArrays(self, A, B, C):
        i=0
        j=0
        k=0
        
        #C.clear()
        while(i<len(A) and j<len(B)):
            if(A[i]>B[j]):
                C[k]=B[j]
                j+=1
                k+=1
            else:
                #C.append(A[i])
                C[k]=A[i]
                
                k+=1
                i+=1
                
        
        
        while(i<len(A)):
            C[k]=A[i]
            k+=1
                
            i+=1
                
       
        
        while(j<len(B)):
            C[k]=B[j]
            k+=1
                
            j+=1
                
        return C


# In[ ]:




