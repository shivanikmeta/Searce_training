#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Partioning an array

class Solution:
    def partition(self, A, pivot):
        i=-1
        j=0
        end=len(A)
        while(j<end):
            if(A[j]>A[pivot]):
                j=j+1
            else:
                i=i+1
                temp=A[i]
                A[i]=A[j]
                A[j]=temp
                j=j+1


# In[2]:


#implementing Quick Sort

class Solution:
    def quicksort(self, Arr):
        end=len(Arr)-1
        start=0
        self.quickSort(Arr,start,end)
        return Arr
        
    def quickSort(self,Arr,start,end):
        
        
        if (end-start) <= 0:
            return Arr
        elif(end-start) >= 0:   
            pivot=end
            pivot_position = self.partition(Arr,pivot)
            self.quickSort(Arr,start,pivot_position-1)
            self.quickSort(Arr,pivot_position+1,end)
    def partition(self, A, pivot):
        j=0
        i=-1
        

        while(j<=pivot):
            if int(A[j])>int(A[pivot]):
                j=j+1
            else:
                i=i+1
                
                A[j],A[i]=A[i],A[j]
                j=j+1
        return i


# In[ ]:




