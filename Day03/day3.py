path = './input.txt'

with open(path,'r') as f:
    lines = f.readlines()
    r1d1 = 0
    r3d1 = 0
    r5d1 = 0
    r7d1 = 0
    r1d2 = 0
    i = 0
    lineLen = len(lines[0].strip())
    for line in lines:
        if line.strip()[(3*i)%(lineLen)] == '#':
            r3d1 += 1
        if line.strip()[i%lineLen] == '#':
            r1d1 += 1
        if line.strip()[(5*i)%lineLen] == '#':
            r5d1 += 1
        if line.strip()[(7*i)%lineLen] == '#':
            r7d1 += 1
        if (i%2==0):
            if (line.strip()[int(i/2)%lineLen] == '#'):
                r1d2 += 1
        i += 1

print(r3d1)
print(r1d1*r3d1*r5d1*r7d1*r1d2)


