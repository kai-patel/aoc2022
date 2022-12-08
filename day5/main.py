#!/usr/bin/env python
# coding: utf-8

# In[50]:


import itertools
from collections import deque
import re

def is_boxes(line):
    return line.strip().startswith('[')

# Deque left is top of stack


# In[51]:


# Part 1
with open("input.txt", "r") as f:
    layers = []
    n_stacks = None
    stacks = []
    
    lines = f.readlines()
    for line in lines:
        if is_boxes(line):
            spaced = line.rstrip('\n').split('    ')
            sep = list(itertools.chain.from_iterable([i.split(' ') for i in spaced]))
            layers.append(sep)
        else:
            if line.lstrip().startswith('1'):
                n_stacks = int(line.split()[-1])
                stacks = [deque() for _ in range(n_stacks)]
                
                for i in range(n_stacks):
                    for layer in layers:
                        if layer[i] != '':
                            stacks[i].append(layer[i])
                # print(stacks)
            
            if line.startswith('move'):
                n, src, dst = map(int, re.findall(r'\d+', line))
                # print([n, src, dst])
                for i in range(n):
                    crate = stacks[src-1].popleft()
                    stacks[dst-1].appendleft(crate)
                    
                # print(stacks)
                
    print(''.join(stack[0].lstrip('[').rstrip(']') for stack in stacks))


# In[54]:


# Part 2
with open("input.txt", "r") as f:
    layers = []
    n_stacks = None
    stacks = []
    
    lines = f.readlines()
    for line in lines:
        if is_boxes(line):
            spaced = line.rstrip('\n').split('    ')
            sep = list(itertools.chain.from_iterable([i.split(' ') for i in spaced]))
            layers.append(sep)
        else:
            if line.lstrip().startswith('1'):
                n_stacks = int(line.split()[-1])
                stacks = [deque() for _ in range(n_stacks)]
                
                for i in range(n_stacks):
                    for layer in layers:
                        if layer[i] != '':
                            stacks[i].append(layer[i])
                # print(stacks)
            
            if line.startswith('move'):
                n, src, dst = map(int, re.findall(r'\d+', line))
                # print([n, src, dst])
                tmp = []
                for i in range(n):
                    crate = stacks[src-1].popleft()
                    tmp.append(crate)
                    
                for i in tmp[::-1]:
                    stacks[dst-1].appendleft(i)
                    
                # print(stacks)
                
    print(''.join(stack[0].lstrip('[').rstrip(']') for stack in stacks))


# In[ ]:




