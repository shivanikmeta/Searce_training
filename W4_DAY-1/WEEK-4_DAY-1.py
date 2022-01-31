#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Push into a Stack

class Stack:
   def __init__(self):
      self.stack = []

   def add(self, dataval):
#  list append method to add element
      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False
#  peek to look at the top of the stack
   def peek(self):     
	   return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())


# In[2]:


#POP from a stack

class Stack:
   def __init__(self):
      self.stack = []

   def add(self, dataval):
#  append method to add element
      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False
        
#  pop method to remove element
   def remove(self):
      if len(self.stack) <= 0:
         return ("No element in the Stack")
      else:
         return self.stack.pop()
        

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())


# In[ ]:




