from collections import defaultdict

path = './inputTest.txt'

with open(path) as f:
    lines = f.readlines()
    p1 = 0
    p2 = 0
    for line in lines:
        words = line.strip().split()
        lo, hi = [int(x) for x in words[0].split('-')]
        chReq = words[1][0]
        password = words[2]
        counts = defaultdict(int)
        for ch in password:
            counts[ch] += 1
        if lo <= counts[chReq] <= hi:
            p1 += 1
        if ((password[lo-1] == chReq) ^
                (password[hi-1] == chReq)):  # ^ is the xor symbol
            p2 += 1

print(p1, p2)


print(counts)
print(password)
