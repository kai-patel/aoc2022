import sys

if not sys.argv[1]:
    print("Please supply an input file")

# Part 1
with open(sys.argv[1], 'r') as f:
    rounds = f.readlines()
    total = 0
    for r in rounds:
        them, us = r.split()
        # print(them, us)
        if us == 'X':
            total += 1
        elif us == 'Y':
            total += 2
        elif us == 'Z':
            total += 3
            
        if (them == 'A' and us == 'X') or (them == 'B' and us == 'Y') or (them == 'C' and us == 'Z'):
            total += 3
        elif them == 'A':
            if us == 'Z':
                total += 0
            else:
                total += 6
        elif them == 'B':
            if us == 'X':
                total += 0
            else:
                total += 6
        elif them == 'C':
            if us == 'Y':
                total += 0
            else:
                total += 6
        
        # print(total)
                
    print(total)

# Part 2
with open(sys.argv[1], 'r') as f:
    rounds = f.readlines()
    total = 0
    for r in rounds:
        them, us = r.split()
        
        if them == 'A':
            if us == 'X':
                total += 0
                total += 3
            elif us == 'Y':
                total += 3
                total += 1
            elif us == 'Z':
                total += 6
                total += 2
                
        if them == 'B':
            if us == 'X':
                total += 0
                total += 1
            elif us == 'Y':
                total += 3
                total += 2
            elif us == 'Z':
                total += 6
                total += 3
                
        if them == 'C':
            if us == 'X':
                total += 0
                total += 2
            elif us == 'Y':
                total += 3
                total += 3
            elif us == 'Z':
                total += 6
                total += 1

print(total)