path = './inputTestSmall.txt'

with open(path) as f:
    lines = sorted([int(i) for i in f])
    lines.insert(0, int(0))
    lines.append(max(lines) + 3)

oneJ = 0
threeJ = 0

for i in range(1, len(lines)):
    if lines[i] - lines[i-1] == 1:
        oneJ += 1
    elif lines[i] - lines[i-1] == 3:
        threeJ += 1

print(oneJ * threeJ)


DP = {}


def dp(i):
    if i == len(lines) - 1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(lines)):
        if lines[j] - lines[i] <= 3:
            ans += dp(j)
        else:
            break
    DP[i] = ans
    return ans


print(dp(0))
