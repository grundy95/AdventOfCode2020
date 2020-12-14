from copy import deepcopy

path = './input.txt'

with open(path) as f:
    G = []
    for line in f:
        newLine = list(line.strip())
        newLine.append('.')
        newLine.insert(0, '.')
        G.append(newLine)
    dotLine = []
    for i in range(len(G[0])):
        dotLine.append('.')
    G.append(dotLine)
    G.insert(0,dotLine)

    # G.append(np.repeat('.', len(G[1])))
    # G.insert(0, np.repeat('.', len(G[1])))

whileCount = 1
while True:
    Gnew = copy.deepcopy(G)
    for i in range(1, len(G) - 1):
        for j in range(1, len(G[0]) - 1):
            if G[i][j] != '.':
                empty = 0
                taken = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k == i and l == j:
                            continue
                        elif G[k][l] == 'L':
                            empty += 1
                        elif G[k][l] == '#':
                            taken += 1
                if G[i][j] == 'L' and taken == 0:
                    Gnew[i][j] = '#'
                elif G[i][j] == '#' and taken >= 4:
                    Gnew[i][j] = 'L'

    if Gnew == G:
        break
    else:
        G = copy.deepcopy(Gnew)
        whileCount += 1

print('whilecount:', whileCount)
p1 = 0
for i in range(len(G)):
    for j in range(len(G[0])):
        if Gnew[i][j] == '#':
            p1 += 1
print(p1)




