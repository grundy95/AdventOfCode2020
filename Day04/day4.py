import re
path = './input.txt'


with open(path) as f:
    lines = f.read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optionalFields = ['cid']

p1 = 0
p2 = 0
hclCount = 0
for line in lines:
    line = line.replace('\n', ' ')
    # print(line)
    passport = all(elem in line for elem in fields)
    if passport:
        p1 += 1

        byrValid = 1920 <= int(line.split('byr:', 1)[1][:4]) <= 2002
        iyrValid = 2010 <= int(line.split('iyr:', 1)[1][:4]) <= 2020
        eyrValid = 2020 <= int(line.split('eyr:', 1)[1][:4]) <= 2030
        height = line.split('hgt:', 1)[1].split(' ')[0]
        if height[-2:] == 'cm':
            hgtValid = 150 <= int(height.split('cm')[0]) <= 193
        elif height[-2:] == 'in':
            hgtValid = 59 <= int(height.split('in')[0]) <= 76
        else:
            hgtValid = False
        hclFormat = re.compile('^#[0-9a-f]{6}')
        if hclFormat.match(line.split('hcl:', 1)[1]):
            hclValid = True
        else:
            hclValid = False
        eclFields = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        eclValid = any(elem in line.split('ecl:', 1)[1].split(' ')[0]
                       for elem in eclFields)
        pidFormat = re.compile('^[0-9]{9}$')
        if pidFormat.match(line.split('pid:', 1)[1].split(' ')[0]):
            pidValid = True
        else:
            pidValid = False
        if (byrValid and iyrValid and eyrValid and hgtValid
                and hclValid and eclValid and pidValid):
            p2 += 1

print(p1)
print(p2)
