path = './input.txt'

with open(path) as f:
    lines = [line.strip() for line in f]


def solvePart1():
    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]
    x = 0
    y = 0
    dir_ = 1
    for line in lines:
        cmd = line[0]
        n = int(line[1:])
        if cmd == 'N':
            y += n
        elif cmd == 'S':
            y -= n
        elif cmd == 'E':
            x += n
        elif cmd == 'W':
            x -= n

        elif cmd == 'L':
            for i in range(int(n / 90)):
                dir_ = (dir_ + 3) % 4

        elif cmd == 'R':
            for i in range(int(n / 90)):
                dir_ = (dir_ + 1) % 4

        elif cmd == 'F':
            x += DX[dir_] * n
            y += DY[dir_] * n
    return abs(x) + abs(y)


def solvePart2():
    wx = 10
    wy = 1
    x = 0
    y = 0
    for line in lines:
        cmd = line[0]
        n = int(line[1:])
        if cmd == 'N':
            wy += n
        elif cmd == 'S':
            wy -= n
        elif cmd == 'E':
            wx += n
        elif cmd == 'W':
            wx -= n

        elif cmd == 'L':
            for i in range(int(n / 90)):
                wx, wy = -wy, wx

        elif cmd == 'R':
            for i in range(int(n / 90)):
                wx, wy = wy, -wx

        elif cmd == 'F':
            x += n * wx
            y += n * wy

    return abs(x) + abs(y)


print(solvePart1())
print(solvePart2())
