from collections import defaultdict

path = './input.txt'


with open(path) as f:
    lines = list(f)

countSumAny = 0
countSumAll = 0
lines.append(' ')
group = defaultdict(int)
groupSize = 0
for line in lines:
    line = line.strip()
    if not line:
        countSumAny += len(group)
        # newGroup = {k:v for (k, v) in group.items() if v >= groupSize}
        # print(newGroup)
        countSumAll += len({k:v for (k, v) in group.items() if v >= groupSize})
        # print(len({(k, v) for k, v in group.items() if v >= groupSize}))

        group = defaultdict(int)
        newGroup = defaultdict(int)
        groupSize = 0
    else:
        for letters in line:
            group[letters] += 1
        groupSize += 1

print(countSumAny)
print(countSumAll)
