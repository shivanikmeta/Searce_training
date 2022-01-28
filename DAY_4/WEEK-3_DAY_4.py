#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Implementing Linear Search

def Lsearch(n,A,key):
    
    found=False
    for i in range(n):
        if(int(A[i])==(key)):
            index=i
            found=True
            
    if found:
             print(index)
    else:
        print("No")
            
n=int(input())
A=input().split()
key=int(input())
Lsearch(n,A,key)


# In[ ]:


#Finding element using Binary search
def bsearch(n,A,key):
    
    low=0
    high=n-1
    mid=0
    
    while(key!=A[mid] and low<high):
        mid=(low+high)//2
        
        if(key==A[mid]):
            print("1")
            return
        elif(key>A[mid]):
            low=mid+1
        elif(key<A[mid]):
            high=mid-1
    
    print("-1")

