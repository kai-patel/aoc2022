#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check_cycle(cycle, x):
    if cycle > 0 and (cycle == 20 or (cycle - 20) % 40 == 0):
        print(cycle, total, x, cycle * x)
        return cycle * x
    
    return 0

# Part 1
with open("input.txt", "r") as f:
    lines = f.readlines()
    i = 0
    cycle = 0
    x = 1
    total = 0
    
    while i < len(lines):
        cycle += 1
        total += check_cycle(cycle, x)
        
        tokens = lines[i].split()       
        match tokens[0]:
            case 'noop':
                pass
            case 'addx':
                cycle += 1
                total += check_cycle(cycle, x)
                x += int(tokens[1])

        i += 1
        
    
    print(total)


# In[ ]:


# Part 2
with open("input.txt", "r") as f:
    lines = f.readlines()
    i = 0
    cycle = 0
    x = 1
    total = 0
    pixels = ['o' for _ in range(40*6)]
    
    while i < len(lines):
        cycle += 1
        
        if abs((cycle - 1) % 40 - x) <= 1:
            pixels[cycle - 1] = '#'
        else:
            pixels[cycle - 1] = '.'
        
        tokens = lines[i].split()       
        match tokens[0]:
            case 'noop':
                pass
            case 'addx':
                cycle += 1
                # total += check_cycle(cycle, x)
                if abs((cycle - 1) % 40 - x) <= 1:
                    pixels[cycle - 1] = '#'
                else:
                    pixels[cycle - 1] = '.'

                x += int(tokens[1])

        i += 1
        
    
    image = [pixels[i:i+40] for i in range(0, len(pixels), 40)]
    print(len(pixels))
    for row in image:
        print(''.join(row))


# In[ ]:




