#!/usr/bin/env python
# coding: utf-8

# In[28]:


import string
import functools

letters = string.ascii_letters
priorities = [i+1 for i in range(len(letters))]

priority = dict(zip(letters, priorities))


# In[29]:


# Part 1
with open("input.txt", "r") as f:
    rucksacks = f.readlines()
    total = 0
    for rucksack in rucksacks:
        compart1, compart2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        item = list(set(compart1).intersection(set(compart2)))[0]
        total += priority[item]
        
    print(total)


# In[34]:


# Part 2
with open("input.txt", "r") as f:
    elves = f.readlines()
    total = 0
    for i in range(0, len(elves), 3):
        group = elves[i:i+3]
        badge = list(functools.reduce(lambda x, y: x.intersection(y), map(lambda x: set(x.strip()), group)))[0]
        total += priority[badge]
    print(total)


# In[ ]:




