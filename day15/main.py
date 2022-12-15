#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import itertools
import functools
from collections import Counter

class Sensor:
    position = None
    nearest = None
    distance = -1
    border_points = None
    
    def __init__(self, position, nearest):
        self.position = position
        self.nearest = nearest
        self.distance = abs(position[0] -  nearest[0]) + abs(position[1] - nearest[1])
        # self.border_points = self.points()
        
    def distance_to(self, point):
        return abs(self.position[0] - point[0]) + abs(self.position[1] - point[1])
    
    def covers(self, point):
        return self.distance_to(point) <= self.distance
    
    def points(self):
        # print("Getting border")
        res = set()
        for y in range(self.position[1] - (self.distance), self.position[1] + self.distance):
            if y < 0:
                continue
            if y > 4000000:
                break
            D_min_ys = (self.distance + 1) - abs(y - self.position[1])
            x1 = self.position[0]
            a = (D_min_ys) + x1
            b = (-1*(D_min_ys)) + x1

            if 0 <= a <= 4000000:
                res.add((a, y))
            if 0 <= b <= 4000000:
                res.add((b, y))
            
        return res
    
    def __str__(self):
        return f"sx={self.position[0]}, sy={self.position[1]} --- bx={self.nearest[0]}, by={self.nearest[1]} - db={self.distance}"
    
    def __repr__(self):
        return str(self)


# In[ ]:


with open("input.txt", "r") as f:
    lines = f.readlines()
    sensors = []
    used = set()
    beacons = set()
    
    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        
        used.add((sx, sy))
        beacons.add((bx, by))
        
        sensor = Sensor((sx, sy), (bx, by))
        sensors.append(sensor)
        
    total = 0
    covered = set()
    y = 2000000
    
    candidates = [s for s in sensors if s.covers((s.position[0], y))]
    
    i = 0
    for sensor in candidates:
        print(i+1)
        D_min_ys = sensor.distance - abs(y - sensor.position[1])
        x1 = sensor.position[0]
        a = (D_min_ys) + x1
        b = (-1*(D_min_ys)) + x1
        
        a, b = sorted([a, b])
        # print((a, b))
        for x in range(a, b + 1):
            if (x, y) not in beacons and (x, y) not in used:
                covered.add((x, y))
        i += 1
                
    print(len(covered))


# In[ ]:


# Part 2   
with open("input.txt", "r") as f:
    lines = f.readlines()
    sensors = []
    
    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        
        sensor = Sensor((sx, sy), (bx, by))
        sensors.append(sensor)

    # print("Finding combinations")
    
    combos = itertools.combinations(sensors, 2)
    count = Counter()
    for i, combo in enumerate(combos):
        if i % 1 == 0:
            print(i)
        
        point = functools.reduce(lambda x, y: x.intersection(y.points()), combo, combo[0].points())
        
        
        if len(point) > 0:
            for p in point:
                count[p] += 1
                
    print(count.most_common(1))

ans = count.most_common(1)[0]
print(ans[0][0] * 4000000 + ans[0][1])
# In[ ]:


ans = (2949122 * 4000000) + 3041245


# In[ ]:


print(ans)


# In[ ]:




