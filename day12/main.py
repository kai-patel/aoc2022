#!/usr/bin/env python
# coding: utf-8

# In[2]:


import itertools
import functools
from collections import deque
from multiprocessing import Pool


def char_to_height(c):
    if c == "S":
        return ord("a")
    elif c == "E":
        return ord("z")

    return ord(c)


def pathfind(grid, h, w, source, dest):
    print(source, flush=True)
    dist = [float("inf") for _ in grid]
    prev = [None for _ in grid]
    q = set()

    for v in range(len(grid)):
        q.add(v)

    dist[source] = 0

    while len(q) > 0:

        best = float("inf")
        u = None
        for v in q:
            if dist[v] <= best:
                best = dist[v]
                u = v

        q.remove(u)

        for v in q:
            if (v == u - w or v == u + w or v == u + 1 or v == u - 1) and (
                grid[v] <= grid[u] + 1
            ):
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist[dest]


# Part 1
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        grid = []
        lines = f.readlines()
        for line in lines:
            row = list(line.strip())
            grid.append(row)

        h = len(grid)
        w = len(grid[0])
        source = None
        dest = None

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "S":
                    source = i * w + j
                elif grid[i][j] == "E":
                    dest = i * w + j

        grid = list(map(char_to_height, itertools.chain.from_iterable(grid)))
        print(pathfind(grid, h, w, source, dest))

    # In[ ]:

    # Part 2
    with open("input.txt", "r") as f:
        grid = []
        lines = f.readlines()
        for line in lines:
            row = list(line.strip())
            grid.append(row)

        h = len(grid)
        w = len(grid[0])
        sources = []
        dest = None
        shortest = float("inf")

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "E":
                    dest = i * w + j

        grid = list(map(char_to_height, itertools.chain.from_iterable(grid)))

        for i in range(len(grid)):
            if grid[i] == ord("a"):
                sources.append(i)

        print(len(sources))

        args = [(grid, h, w, s, dest) for s in sources]

        with Pool(8) as p:
            print(min(p.starmap(pathfind, args, 64)))
