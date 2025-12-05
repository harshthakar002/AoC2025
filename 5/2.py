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
def updateRanges(ranges):
    newRanges = [ranges[0]]
    for i in range(1, len(ranges)):
        rangeToMerge = ranges[i]
        hasMerged = False
        for j in range(len(newRanges)):
            mstart, mend = rangeToMerge
            start, end = newRanges[j]
            if mend < start or mstart > end:
                continue
            else:
                newRanges[j] = min(start, mstart), max(end, mend)
                hasMerged = True
                break
        if not hasMerged:
            newRanges.append(rangeToMerge)
    return newRanges, len(ranges) != len(newRanges)
ranges, hasMerged = updateRanges(ranges)
while hasMerged:
    ranges, hasMerged = updateRanges(ranges)
count = 0
for start, end in ranges:
    count += end - start + 1
print(count)
                
