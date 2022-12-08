#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Part 1
with open("input.txt", "r") as f:
    text = f.read().strip()
    # print(text)
    
    for i in range(len(text)):
        window = text[i:i+4]
        if len(set(window)) == len(window):
            print(i+4)
            print(set(window))
            break


# In[35]:


# Part 1
with open("input.txt", "r") as f:
    text = f.read().strip()
    print(text)
    
    for i in range(len(text)):
        window = text[i:i+14]
        if len(set(window)) == len(window):
            print(i+14)
            print(set(window))
            break


# In[ ]:




