path = './input.txt'


print('Part 1:\n')
with open(path,'r') as f:
    data = [int(x) for x in f]
    for i in data:
        for j in data:
            # print(i)
            # print(j)
            if i+j == 2020:
                print('The two numbers are', i, 'and', j, '. Their product is', i*j, '\n\n')
                break
        else:
            continue
        break


print('Part 2:\n')
with open(path, 'r') as f:
    data = [int(x) for x in f]
    for i in data:
        for j in data:
            for k in data:
                if i+j+k == 2020:
                    print('The three numbers are', i, j, 'and', k, '. Their product is', i*j*k)
                    break
            else:
                continue
            break
        else:
            continue
        break




