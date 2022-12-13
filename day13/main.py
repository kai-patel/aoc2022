#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import functools

def compare(left, right):
    # print(left, right, type(left), type(right))
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left <= right
    
    if isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left):
            if i >= len(right):
                return False
            if compare(left[i], right[i]) is not None:
                return compare(left[i], right[i])
            i += 1
        return True
        
    
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    
    return True

# Part 1
with open("input.txt", "r") as f:
    lines = f.read()
    pairs = filter(lambda x: len(x) > 1, lines.split('\n\n'))
    
    total = 0
    
    for (i, pair) in enumerate(pairs):
        left, right = map(lambda x: eval(x), pair.strip().split('\n'))
        if compare(left, right):
            total += i + 1
    print(total)


# In[ ]:


# Part 2
def cmp(left, right):
    if compare(left, right) is None:
        return 0
    
    if compare(left, right):
        return 1
    
    return -1

with open("input.txt", "r") as f:
    lines = f.read()
    pairs = filter(lambda x: len(x) > 1, lines.split('\n\n'))
    
    packets = [
        [[2]],
        [[6]]
    ]
    
    for (i, pair) in enumerate(pairs):
        left, right = map(lambda x: eval(x), pair.strip().split('\n'))
        packets.append(left)
        packets.append(right)
    
    order = sorted(packets, key=functools.cmp_to_key(cmp), reverse=True)
    print((order.index([[2]]) + 1) * (order.index([[6]]) + 1))


# In[ ]:




