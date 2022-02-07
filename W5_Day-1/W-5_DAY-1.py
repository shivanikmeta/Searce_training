#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#OOPS
#CALCULATOR class in python

class Calculator:
    def sum(self,A):
        n=len(A)
        sum=0
        for i in range(n):
            sum=sum+A[i]
        return sum
    def minus(self,a,b):
        d = a-b
        return d
    def multiply(self,A):
        fact=1
        n=len(A)
        for i in range(n):
            fact=fact*A[i]
        return fact
    def divide(self,a,b):
        if(b==0):
            return("Div by 0 not allowed!")
        else:
            c=int(a//b)
            return c

