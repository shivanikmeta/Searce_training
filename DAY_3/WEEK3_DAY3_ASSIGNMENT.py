#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math
import os
import random
import re
import sys
from heapq import heappush, heappop


# In[9]:


def minimumAverage(customers):
    
    total_time = waiting_time = 0
    customers.sort(reverse=True)
    queue = []
    
    while customers or queue:
        while customers and customers[-1][0]<total_time:
            heappush(queue, customers.pop()[::-1])
        
        if queue:
            task = heappop(queue)
            total_time+= task[0]
            waiting_time += total_time - task[1]
            
        else:
            heappush(queue, customers.pop()[::-1])
            total_time = queue[0][1]
            
    return waiting_time//n


# In[ ]:




