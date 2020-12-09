path = './input.txt'
with open(path) as f:
    lines = list(f)

lines.append('')
anyYes = None
allYes = None
p1 = 0
p2 = 0

for line in lines:
    line = line.strip()
    if not line:
        p1 += len(anyYes)
        p2 += len(allYes)
        anyYes = None
        allYes = None
    else:
        if anyYes is None:
            anyYes = set(line)
        else:
            anyYes = anyYes | set(line)

        if allYes is None:
            allYes = set(line)
        else:
            allYes = allYes & set(line)

print(p1)
print(p2)
