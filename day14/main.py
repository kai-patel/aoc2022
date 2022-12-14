#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools

# Part 1
with open("input.txt", "r") as f:
    paths = f.readlines()
    rocks = set()
    sands = set()
    for path in paths:
        pairs = path.strip().split(' -> ')
        points = []
        for pair in pairs:
            x, y = map(int, pair.split(','))
            points.append((x, y))
        
        lines = itertools.pairwise(points)
        
        for line in lines:
            x1 = line[0][0]
            x2 = line[1][0]
            y1 = line[0][1]
            y2 = line[1][1]
            
            dx = 1 if x2 >= x1 else -1
            dy = 1 if y2 >= y1 else -1
            
            for x in range(x1, x2 + dx, dx):
                for y in range(y1, y2 + dy, dy):
                    rocks.add((x, y))
                    
    bottom = max(rocks, key=lambda x: x[1])[1]
    
    sand = (500, 0)
    
    while sand[1] < bottom:
        below = (sand[0], sand[1] + 1)
        below_left = (sand[0] - 1, sand[1] + 1)
        below_right = (sand[0] + 1, sand[1] + 1)
        
        if below not in rocks and below not in sands:
            sand = below
        elif below_left not in rocks and below_left not in sands:
            sand = below_left
        elif below_right not in rocks and below_right not in sands:
            sand = below_right
        else:
            sands.add(sand)
            sand = (500, 0)
        
    print(len(sands))


# In[ ]:


# Part 2
with open("input.txt", "r") as f:
    paths = f.readlines()
    rocks = set()
    sands = set()
    for path in paths:
        pairs = path.strip().split(' -> ')
        points = []
        for pair in pairs:
            x, y = map(int, pair.split(','))
            points.append((x, y))
        
        lines = itertools.pairwise(points)
        
        for line in lines:
            x1 = line[0][0]
            x2 = line[1][0]
            y1 = line[0][1]
            y2 = line[1][1]
            
            dx = 1 if x2 >= x1 else -1
            dy = 1 if y2 >= y1 else -1
            
            for x in range(x1, x2 + dx, dx):
                for y in range(y1, y2 + dy, dy):
                    rocks.add((x, y))
                    
    bottom = max(rocks, key=lambda x: x[1])[1] + 2
    
    sand = (500, 0)
    
    while (500, 0) not in sands:
        below = (sand[0], sand[1] + 1)
        below_left = (sand[0] - 1, sand[1] + 1)
        below_right = (sand[0] + 1, sand[1] + 1)
        
        if below not in rocks and below not in sands and below[1] != bottom:
            sand = below
        elif below_left not in rocks and below_left not in sands and below_left[1] != bottom:
            sand = below_left
        elif below_right not in rocks and below_right not in sands and below_right[1] != bottom:
            sand = below_right
        else:
            sands.add(sand)
            sand = (500, 0)
        
    print(len(sands))


# In[ ]:




