path = './input.txt'

with open(path) as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = [lines[i][0], int(lines[i][1:])]

sp = [0, 0]
sp2 = [0, 0]
wp = [1, 10]
d = ['E', 90]
for line in lines:
    v = line[1]
    if line[0] == 'F':
        if d[0] == 'N':
            sp = [sp[0] + v, sp[1]]
        elif d[0] == 'E':
            sp = [sp[0], sp[1] + v]
        elif d[0] == 'S':
            sp = [sp[0] - v, sp[1]]
        elif d[0] == 'W':
            sp = [sp[0], sp[1] - v]
        sp2 = [sp2[0] + (wp[0] * v), sp2[1] + (wp[1] * v)]

    elif line[0] == 'N':
        sp = [sp[0] + v, sp[1]]
        wp = [wp[0] + v, wp[1]]
    elif line[0] == 'S':
        sp = [sp[0] - v, sp[1]]
        wp = [wp[0] - v, wp[1]]
    elif line[0] == 'E':
        sp = [sp[0], sp[1] + v]
        wp = [wp[0], wp[1] + v]
    elif line[0] == 'W':
        sp = [sp[0], sp[1] - v]
        wp = [wp[0], wp[1] - v]
    elif line[0] == 'L':
        if (d[1] - v) % 360 == 90:
            d = ['E', 90]
        elif (d[1] - v) % 360 == 180:
            d = ['S', 180]
        elif (d[1] - v) % 360 == 270:
            d = ['W', 270]
        elif (d[1] - v) % 360 == 0:
            d = ['N', 0]
        if v == 180:
            wp = [wp[0] * (-1), wp[1] * (-1)]
        elif v == 90:
            wp = [wp[1], wp[0] * (-1)]
        elif v == 270:
            wp = [wp[1] * (-1), wp[0]]
    elif line[0] == 'R':
        if (d[1] + v) % 360 == 90:
            d = ['E', 90]
        elif (d[1] + v) % 360 == 180:
            d = ['S', 180]
        elif (d[1] + v) % 360 == 270:
            d = ['W', 270]
        elif (d[1] + v) % 360 == 0:
            d = ['N', 0]
        if v == 180:
            wp = [wp[0] * (-1), wp[1] * (-1)]
        elif v == 90:
            wp = [wp[1] * (-1), wp[0]]
        elif v == 270:
            wp = [wp[1], wp[0] * (-1)]

print(abs(sp[0])+abs(sp[1]))
print(abs(sp2[0])+abs(sp2[1]))
