#!/usr/bin/env python
# coding: utf-8

# In[4]:


#linked list traversal
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = LinkedList()
list.headval = Node("Jan")
e2 = Node("Feb")
e3 = Node("March")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()


# In[ ]:




