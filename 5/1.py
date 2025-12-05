f = open('./5/inp.txt', 'r')
lines = f.readlines()
i = 0
ranges = []
for i in range(len(lines)):
    line = lines[i].strip()
    if line == '':
        break
    numbers = line.split('-')
    ranges.append((int(numbers[0]), int(numbers[1])))
i = i + 1
count = 0
def isInRange(number, ranges):
    for start,end in ranges:
        if number >= start and number <= end:
            return True
    return False
while i < len(lines):
    if isInRange(int(lines[i]), ranges):
        count += 1
    i +=1
print(count)