#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools

class Node:
    children = {}
    size = None
    name = ""
    parent = None
    
    def __init__(self, name, children, size, parent):
        self.name = name
        self.children = children
        self.size = size
        self.parent = parent
        
    def __str__(self):
        return f"{self.name}: {'dir' if not self.size else self.size} --- Parent: {self.parent.name if self.parent else None}"
    
    def total_size(self):
        total = 0
        for child in self.children.values():
            if child.size:
                total += child.size
            else:
                total += child.total_size()
                
        return total
        
def print_tree(root, indent):
    if not root:
        return
    print(f"{'-|'*indent} {root.name}: {root.size}")
    for child in root.children.values():
        print_tree(child, indent+1)


# In[2]:


root = Node("/", {}, None, None)
current_dir = root

with open("input.txt", "r") as f:
    lines = f.readlines()
    # print(lines)
    for i in range(1, len(lines)):
        line = lines[i].strip()
        # print(current_dir)
        if line.startswith('$'):
            tokens = line.split()
            if tokens[1] == 'ls':
                pass
            elif tokens[1] == 'cd':
                if tokens[2] == "..":
                    current_dir = current_dir.parent
                elif tokens[2] == '/':
                    current_dir = root
                else:
                    current_dir = current_dir.children[tokens[2]]
        else:
            size, name = line.split()
            tmp = current_dir
            current_dir.children[name] = Node(name, {}, None if size == "dir" else int(size), tmp)    

# print_tree(root, 0)
print(root.total_size())


# In[3]:


def part1(root):
    total = 0
    
    def traverse(root):
        nonlocal total
        if not root:
            return

        if root.size:
            return

        # print(root.total_size())

        if root.total_size() <= 100000:
            total += root.total_size()

        for child in root.children.values():
            traverse(child)
            
    traverse(root)
    return total


# In[4]:


total = part1(root)
print(total)


# In[5]:


used = root.total_size()
free = 70000000 - used
required = 30000000 - free
print(used, free, required)


# In[6]:


def part2(root):
    smallest = root
    
    def traverse(root):
        nonlocal smallest
        
        if not root:
            return
        
        if root.size:
            return
        
        if root.total_size() >= required:
            if root.total_size() < smallest.total_size():
                smallest = root
                
        for child in root.children.values():
            traverse(child)
    
    traverse(root)
    return smallest


# In[7]:


smallest = part2(root)


# In[8]:


print(smallest)
print(smallest.total_size())


# In[ ]:




