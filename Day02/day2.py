path = './input.txt'

print('Part 1 \n')
with open(path, 'r') as f:
    data = f.readlines()
    data = [i.replace('-', ' ').replace(':', '').replace('\n', '').split(' ')
            for i in data]
    count = int(0)
    for i in range(len(data)):
        data[i][0] = int(data[i][0])
        data[i][1] = int(data[i][1])
        occurences = data[i][3].count(data[i][2])
        data[i].append((occurences >= data[i][0]) and
                       (occurences <= data[i][1]))
        if data[i][4]:
            count = count+1

print('Number of occurrences is', count, '\n\n')

print('Part 2\n')
with open(path, 'r') as f:
    data = f.readlines()
    data = [i.replace('-', ' ').replace(':', '').replace('\n', '').split(' ')
            for i in data]
    count = int(0)
    for i in range(len(data)):
        data[i][0] = int(data[i][0])
        data[i][1] = int(data[i][1])
        pos1 = data[i][3][data[i][0] - 1] == data[i][2]
        pos2 = data[i][3][data[i][1] - 1] == data[i][2]
        if (pos1 + pos2) == 1:
            count = count + 1
print('Number of correct passwords is', count)
