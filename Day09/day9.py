from collections import deque

path = './input.txt'

with open(path) as f:
    lines = list(f)
lines = [int(i) for i in lines]

Plen = 25
P = deque(lines[:Plen])
p1Test = False

for line in lines[Plen:]:
    p1Test = False
    for i in P:
        complmentary = line - i
        if complmentary in P and complmentary != i:
            p1Test = True
            break
    if p1Test == False:
        p1 = line
        break
    P.popleft()
    P.append(line)
print(p1)

Q = list(deque())
count = 2
foundAns = False
while foundAns == False:
    Q = deque(lines[:count])
    for line in lines[count:]:
        if sum(Q) == p1:
            print(Q)
            foundAns = True
            p2 = max(Q) + min(Q)
            break
        Q.popleft()
        Q.append(line)
    count += 1
    if foundAns:
        break

print(p2)
