#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Part 1
head = (0,0)
tail = (0,0)
visited = set()
visited.add(tail)

with open("input.txt", "r") as f:
    motions = f.readlines()
    for motion in motions:
        direction, steps = motion.split()
        steps = int(steps)
        
        match direction:
            case 'U':
                for i in range(steps):
                    head = (head[0], head[1] + 1)
                    dx = head[0] - tail[0]
                    dy = head[1] - tail[1]
                    
                    if abs(dx) >= 2 and dy == 0:
                        tail = (tail[0] + (1 if dx > 0 else -1), tail[1])
                    elif abs(dy) >= 2 and dx == 0:
                        tail = (tail[0], tail[1] + (1 if dy > 0 else -1))
                    elif abs(dx) >= 2 and dy != 0:
                        tail = (tail[0] + (1 if dx > 0 else - 1), tail[1] + (1 if dy > 0 else - 1))
                    elif abs(dy) >= 2 and dx != 0:
                        tail = (tail[0] + (1 if dx > 0 else - 1), tail[1] + (1 if dy > 0 else - 1))
                        
                    visited.add(tail)
            case 'D':
                for i in range(steps):
                    head = (head[0], head[1] - 1)
                    dx = head[0] - tail[0]
                    dy = head[1] - tail[1]
                    
                    if abs(dx) >= 2 and dy == 0:
                        tail = (tail[0] + (1 if dx > 0 else -1), tail[1])
                    elif abs(dy) >= 2 and dx == 0:
                        tail = (tail[0], tail[1] + (1 if dy > 0 else -1))
                    elif abs(dx) >= 2 and dy != 0:
                        tail = (tail[0] + (1 if dx > 0 else - 1), tail[1] + (1 if dy > 0 else - 1))
                    elif abs(dy) >= 2 and dx != 0:
                        tail = (tail[0] + (1 if dx > 0 else - 1), tail[1] + (1 if dy > 0 else - 1))

                    visited.add(tail)                        
            case 'L':
                for i in range(steps):
                    head = (head[0] - 1, head[1])
                    dx = head[0] - tail[0]
                    dy = head[1] - tail[1]
                    
                    if abs(dx) >= 2 and dy == 0:
                        tail = (tail[0] + (1 if dx > 0 else -1), tail[1])
                    elif abs(dy) >= 2 and dx == 0:
                        tail = (tail[0], tail[1] + (1 if dy > 0 else -1))
                    elif abs(dx) >= 2 and dy != 0:
                        tail = (tail[0] + (1 if dx > 0 else - 1), tail[1] + (1 if dy > 0 else - 1))
                    elif abs(dy) >= 2 and dx != 0:
                        tail = (tail[0] + (1 if dx > 0 else - 1), tail[1] + (1 if dy > 0 else - 1))
                    
                    visited.add(tail)            
            case 'R':
                for i in range(steps):
                    head = (head[0] + 1, head[1])
                    dx = head[0] - tail[0]
                    dy = head[1] - tail[1]
                    
                    if abs(dx) >= 2 and dy == 0:
                        tail = (tail[0] + (1 if dx > 0 else -1), tail[1])
                    elif abs(dy) >= 2 and dx == 0:
                        tail = (tail[0], tail[1] + (1 if dy > 0 else -1))
                    elif abs(dx) >= 2 and dy != 0:
                        tail = (tail[0] + (1 if dx > 0 else - 1), tail[1] + (1 if dy > 0 else - 1))
                    elif abs(dy) >= 2 and dx != 0:
                        tail = (tail[0] + (1 if dx > 0 else - 1), tail[1] + (1 if dy > 0 else - 1))
                    
                    visited.add(tail)

    print(len(visited))


# In[35]:


# Part 2

knots = [(0, 0) for i in range(10)]
head = knots[0]
tail = knots[-1]

visited = set()
visited.add(tail)

with open("input.txt", "r") as f:
    motions = f.readlines()
    for motion in motions:
        direction, steps = motion.split()
        steps = int(steps)
        
        match direction:
            case 'U':
                for i in range(steps):
                    head = knots[0]                    
                    head = (head[0], head[1] + 1)
                    knots[0] = head
                    
                    for j in range(1, len(knots)):
                        parent = knots[j - 1]
                        child = knots[j]
                    
                        dx = parent[0] - child[0]
                        dy = parent[1] - child[1]

                        if abs(dx) >= 2 and dy == 0:
                            child = (child[0] + (1 if dx > 0 else -1), child[1])
                        elif abs(dy) >= 2 and dx == 0:
                            child = (child[0], child[1] + (1 if dy > 0 else -1))
                        elif abs(dx) >= 2 and dy != 0:
                            child = (child[0] + (1 if dx > 0 else - 1), child[1] + (1 if dy > 0 else - 1))
                        elif abs(dy) >= 2 and dx != 0:
                            child = (child[0] + (1 if dx > 0 else - 1), child[1] + (1 if dy > 0 else - 1))
                            
                        knots[j] = child    
                        if j == len(knots) - 1:
                            visited.add(knots[-1])
            case 'D':
                for i in range(steps):
                    head = knots[0]                    
                    head = (head[0], head[1] - 1)
                    knots[0] = head
                    
                    for j in range(1, len(knots)):
                        parent = knots[j - 1]
                        child = knots[j]
                    
                        dx = parent[0] - child[0]
                        dy = parent[1] - child[1]

                        if abs(dx) >= 2 and dy == 0:
                            child = (child[0] + (1 if dx > 0 else -1), child[1])
                        elif abs(dy) >= 2 and dx == 0:
                            child = (child[0], child[1] + (1 if dy > 0 else -1))
                        elif abs(dx) >= 2 and dy != 0:
                            child = (child[0] + (1 if dx > 0 else - 1), child[1] + (1 if dy > 0 else - 1))
                        elif abs(dy) >= 2 and dx != 0:
                            child = (child[0] + (1 if dx > 0 else - 1), child[1] + (1 if dy > 0 else - 1))
                            
                        knots[j] = child
                        
                        if j == len(knots) - 1:
                            visited.add(knots[-1])
            case 'L':
                for i in range(steps):
                    head = knots[0]                    
                    head = (head[0] - 1, head[1])
                    knots[0] = head
                    
                    for j in range(1, len(knots)):
                        parent = knots[j - 1]
                        child = knots[j]
                    
                        dx = parent[0] - child[0]
                        dy = parent[1] - child[1]

                        if abs(dx) >= 2 and dy == 0:
                            child = (child[0] + (1 if dx > 0 else -1), child[1])
                        elif abs(dy) >= 2 and dx == 0:
                            child = (child[0], child[1] + (1 if dy > 0 else -1))
                        elif abs(dx) >= 2 and dy != 0:
                            child = (child[0] + (1 if dx > 0 else - 1), child[1] + (1 if dy > 0 else - 1))
                        elif abs(dy) >= 2 and dx != 0:
                            child = (child[0] + (1 if dx > 0 else - 1), child[1] + (1 if dy > 0 else - 1))
                            
                        knots[j] = child
                        if j == len(knots) - 1:
                            visited.add(knots[-1])   
            case 'R':
                for i in range(steps):
                    head = knots[0]                    
                    head = (head[0] + 1, head[1])
                    knots[0] = head
                    
                    for j in range(1, len(knots)):
                        parent = knots[j - 1]
                        child = knots[j]
                    
                        dx = parent[0] - child[0]
                        dy = parent[1] - child[1]

                        if abs(dx) >= 2 and dy == 0:
                            child = (child[0] + (1 if dx > 0 else -1), child[1])
                        elif abs(dy) >= 2 and dx == 0:
                            child = (child[0], child[1] + (1 if dy > 0 else -1))
                        elif abs(dx) >= 2 and dy != 0:
                            child = (child[0] + (1 if dx > 0 else - 1), child[1] + (1 if dy > 0 else - 1))
                        elif abs(dy) >= 2 and dx != 0:
                            child = (child[0] + (1 if dx > 0 else - 1), child[1] + (1 if dy > 0 else - 1))
                            
                        knots[j] = child
                        if j == len(knots) - 1:
                            visited.add(knots[-1])
                    
    print(len(visited))


# In[ ]:




