#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import math

class Monkey:
    n = -1
    inspections = 0
    items = []
    operation = None
    test = None
    if_true = None
    if_false = None
    
    def __str__(self):
        return f"Monkey {self.n}:\n\t- Inspections: {self.inspections}\n\t- {self.items}\n\t- {self.operation}\n\t- {self.test}\n\t\t- {self.if_true}\n\t\t- {self.if_false}"
    
    def __repr__(self):
        return f"Monkey {self.n}:\n\t- Inspections: {self.inspections}\n\t- {self.items}\n\t- {self.operation}\n\t- {self.test}\n\t\t- {self.if_true}\n\t\t- {self.if_false}"
    
# Part 1
with open("input.txt", "r") as f:
    monkeys = []
    lines = f.read()
    chunked = lines.split('\n\n')
    for i, chunk in enumerate(chunked):
        specs = chunk.split('\n')
        monkey = Monkey()
        monkey.n = i
        monkey.items = list(map(int, re.findall(r'\d+', specs[1])))
        monkey.operation = specs[2].split("Operation: ")[1].split('=')[-1]
        monkey.test = int(re.findall(r'\d+', specs[3])[0])
        monkey.if_true = int(re.findall(r'\d+', specs[4])[0])
        monkey.if_false = int(re.findall(r'\d+', specs[5])[0])
        monkeys.append(monkey)
        
    for i in range(20):
        print(f"Round {i+1}")
        # for monkey in monkeys:
        #     print(monkey)
        
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                old = item
                new = eval(monkey.operation)
                new = new // 3
                
                if new % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(new)
                else:
                    monkeys[monkey.if_false].items.append(new)
                
                monkey.items = monkey.items[1:]
      
    
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspections)
    
    print(math.prod(sorted(inspections, reverse=True)[0:2]))


# In[ ]:


with open("input.txt", "r") as f:
    monkeys = []
    lines = f.read()
    chunked = lines.split('\n\n')
    for i, chunk in enumerate(chunked):
        specs = chunk.split('\n')
        monkey = Monkey()
        monkey.n = i
        monkey.items = list(map(int, re.findall(r'\d+', specs[1])))
        monkey.operation = specs[2].split("Operation: ")[1].split('=')[-1]
        monkey.test = int(re.findall(r'\d+', specs[3])[0])
        monkey.if_true = int(re.findall(r'\d+', specs[4])[0])
        monkey.if_false = int(re.findall(r'\d+', specs[5])[0])
        monkeys.append(monkey)
        
    modulus = math.prod([monkey.test for monkey in monkeys]) 
    for i in range(10000):
        if (i+1) % 1000 == 0:
            print(f"Round {i+1}")
        # for monkey in monkeys:
        #     print(monkey)
        
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                old = item
                new = eval(monkey.operation)
                new = new % modulus
                
                if new % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(new)
                else:
                    monkeys[monkey.if_false].items.append(new)
                
                monkey.items = monkey.items[1:]
      
    
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspections)
    
    print(inspections)
    (inspections)
    print(math.prod(sorted(inspections, reverse=True)[0:2]))


# In[ ]:




