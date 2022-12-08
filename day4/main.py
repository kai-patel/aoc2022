#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Part 1
with open("input.txt", "r") as f:
    assignments = f.readlines()
    total = 0
    for assignment in assignments:
        section1, section2 = assignment.split(',')
        x1, y1 = map(int, section1.split('-'))
        x2, y2 = map(int, section2.split('-'))
        
        if (x1 <= x2 and y1 >= y2) or (x2 <= x1 and y2 >= y1):
            total += 1
            
    print(total)


# In[21]:


with open("input.txt", "r") as f:
    assignments = f.readlines()
    total = 0
    for assignment in assignments:
        section1, section2 = assignment.split(',')
        x1, y1 = map(int, section1.split('-'))
        x2, y2 = map(int, section2.split('-'))
        
        if x1 <= y2 and x2 <= y1:
            total += 1
            
    print(total)


# In[ ]:




