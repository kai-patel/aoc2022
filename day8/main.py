#!/usr/bin/env python
# coding: utf-8

# In[21]:


import itertools

def is_visible(tree, path):
    return all(x < tree for x in path)

# Part 1
with open("input.txt", "r") as f:
    lines = f.readlines()
    grid = list(map(lambda x: list(x.strip()), lines))
    h = len(grid)
    w = len(grid[0])
    
    total = 0
    
#     for i in range(1, h - 1):
#         for j in range(1, w - 1):
#             print(grid[i][j], end=", ")
#         print()
        
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            up = [int(grid[r][j]) for r in range(i) if r != i]
            down = [int(grid[r][j]) for r in range(i+1, h) if r != i]
            left = [int(grid[i][c]) for c in range(j) if c != j]
            right = [int(grid[i][c]) for c in range(j+1, w) if c != j]
            paths = [up, down, left, right]
            
            tree = int(grid[i][j])
            
            if any(is_visible(tree, path) for path in paths):
                total += 1
                
    print(total + (2*(h+w) - 4))


# In[52]:


# Part 2
with open("input.txt", "r") as f:
    lines = f.readlines()
    grid = list(map(lambda x: list(x.strip()), lines))
    h = len(grid)
    w = len(grid[0])
    
    best = 0
    pos = (None,None)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            up = list(reversed([int(grid[r][j]) for r in range(i) if r != i]))
            down = [int(grid[r][j]) for r in range(i+1, h) if r != i]
            left = list(reversed([int(grid[i][c]) for c in range(j) if c != j]))
            right = [int(grid[i][c]) for c in range(j+1, w) if c != j]
            paths = [up, down, left, right]
            
            tree = int(grid[i][j])
            
            score = 1
            
            for path in paths:
                tmp = 0
                for x in path:
                    if x < tree:
                        tmp += 1
                    else:
                        tmp += 1
                        break
                if i == 2 and j == 1:
                    print(tmp, path)

                score *= tmp
                    
            if score > best:
                best = score
                pos = (i, j)
                
    print(best, pos)


# In[ ]:




