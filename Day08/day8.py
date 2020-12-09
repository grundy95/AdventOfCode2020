path = './input.txt'

with open(path) as f:
    lines = f.readlines()

def programme(instructions):
    visitedLines = []
    i = 0
    acc = 0
    while i not in visitedLines:
        visitedLines.append(i)
        k, v = instructions[i].split()[0], instructions[i].split()[1]
        if v.startswith('+'):
            v = int(v[1:])
        else:
            v = int(v)
        # print(k, v)
        if k == 'nop':
            i += 1
        elif k == 'acc':
            i += 1
            acc += v
        elif k == 'jmp':
            i += v
        # print(i)
        if i == len(instructions):
            break
    return([i, acc])


codeLen = len(lines)
for j in range(codeLen):
    # print('j:', j)
    # print(lines)
    newLines = lines[:]
    # print(newLines)
    if lines[j].split()[0] == 'nop':
        newLines[j] = 'jmp ' + lines[j].split()[1] + '\n'
        # print(newLines)
        ans = programme(newLines)
        # print(ans)
        if ans[0] == codeLen:
            print(ans[1])
    elif lines[j].split()[0] == 'jmp':
        newLines[j] = 'nop ' + lines[j].split()[1] + '\n'
        # print(newLines)
        ans = programme(newLines)
        # print(ans)
        if ans[0] == codeLen:
            print(ans[1])


# print(lines)
# print(programme(lines))
