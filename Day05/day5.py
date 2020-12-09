# from day5Functions import front, back
import day5Functions


# path = './inputTest.txt'
path = './input.txt'

with open(path) as f:
    lines = f.readlines()

seat = []
seatID = []
maxSeatID = 0
for line in lines:
    line = line.strip()
    rows = [0, 127]
    for letter in line[:-3]:
        if(letter == 'F'):
            rows = day5Functions.front(rows[0], rows[1])
        elif(letter == 'B'):
            rows = day5Functions.back(rows[0], rows[1])
        else:
            print('Error')
    row = rows[0]
    cols = [0, 7]
    for letter in line[-3:]:
        if(letter == 'L'):
            cols = day5Functions.front(cols[0], cols[1])
        elif(letter == 'R'):
            cols = day5Functions.back(cols[0], cols[1])
        else:
            print('Error')
    col = cols[0]
    seat.append([row,col])
    seatID.append(row * 8 + col)
    maxSeatID = max(row * 8 + col, maxSeatID)

emptySeat = []
for i in range(127):
    for j in range(7):
        if all([i,j] != c for c in seat):
            emptySeat.append([i,j])

for seats in emptySeat:
    if (seats[0] * 8 + seats[1] - 1 in seatID) and (seats[0] * 8 + seats[1] + 1 in seatID):
        print(seats[0] * 8 + seats[1])
        break
