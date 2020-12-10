import itertools
path = './inputTest.txt'

with open(path) as f:
    lines = sorted([int(i) for i in f])
    lines2 = lines[:]
    lines.insert(0,int(0))
    lines.append(max(lines) + 3)

oneJ = 0
threeJ = 0

for i in range(1, len(lines)):
    if lines[i] - lines[i-1] == 1:
        oneJ += 1
    elif lines[i] - lines[i-1] == 3:
        threeJ += 1

print(oneJ * threeJ)


def valid(adapters):
    adapters.insert(0, int(0))
    adapters.append(max(adapters)+3)
    validity = True
    for i in range(1, len(adapters)):
        if lines[i] - lines[i - 1] > 3:
            validity = False
            break
    return(validity)


# count = 0
# for i in range(len(lines2)):
    # potentialComb = itertools.combinations(lines2, i)
    # for comb in list(potentialComb):
        # if valid(comb):
            # count += 1
# print(count)


