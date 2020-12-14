
path = './inputTest.txt'

with open(path) as f:
    lines = f.readlines()
    dt = int(lines[0])
    buses = lines[1].strip().split(',')
    buses = [elem for elem in buses if elem != 'x']
    buses = [int(x) for x in buses]
    buses2 = lines[1].strip().split(',')

print(buses2)

wait = []
for i in range(len(buses)):
    wait.append(buses[i] - int(dt % buses[i]))

print(buses[wait.index(min(wait))] * min(wait))
