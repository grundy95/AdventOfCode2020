path = './input.txt'

with open(path) as f:
    Grid = []
    for line in f:
        Grid.append(list(line.strip()))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ans = 1
for (dc, dr) in slopes:
    c = 0
    r = 0
    score = 0
    while r < len(Grid):
        c += dc
        r += dr
        if r < len(Grid) and Grid[r][c % len(Grid[r])] == '#':
            score += 1
    ans *= score
    if dc == 3 and dr == 1:
        print(score)
print(ans)
