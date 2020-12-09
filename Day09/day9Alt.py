import itertools

path = './input.txt'

with open(path) as f:
    xs = list([int(x) for x in f])

PRE = 25
p1 = None
for i in range(PRE, len(xs)):
    prev = xs[i-PRE:i]
    if p1 is None and (not any([x+y==xs[i] for x, y in itertools.combinations(prev,2)])):
        p1 = xs[i]
        break

p2 = None
p2Found = False
for i in range(len(xs)):
    for j in range(i+2, len(xs)):
        ys = xs[i:j]
        if sum(ys) == p1 and p2 is None:
            p2 = min(ys) + max(ys)
            p2Found = True
            break
    if p2Found:
        break

print(p1)
print(p2)
