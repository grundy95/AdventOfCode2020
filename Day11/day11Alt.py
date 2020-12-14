from copy import deepcopy

path = './input.txt'

with open(path) as f:
    G = [list(l.strip()) for l in list(f)]

R = len(G)
C = len(G[0])


def solve(G, p1):
    while True:
        newG = deepcopy(G)
        change = False
        for r in range(R):
            for c in range(C):
                taken = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        rr = r + dr
                        cc = c + dc
                        # Part 2
                        while (0 <= rr < R and 0 <= cc < C and G[rr][cc] == '.'
                               and (not p1)):
                            rr = rr + dr
                            cc = cc + dc
                        # End part 2 specific
                        if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == '#':
                            taken += 1

                if G[r][c] == 'L':
                    if taken == 0:
                        newG[r][c] = '#'
                        change = True
                elif G[r][c] == '#' and taken >= (4 if p1 else 5):
                    newG[r][c] = 'L'
                    change = True
        if not change:
            break

        G = deepcopy(newG)

    ans = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] =='#':
                ans += 1

    return ans


print(solve(G, True))
print(solve(G, False))

