f = open('./2/inp.txt', 'r')
l = f.readline()
pairs = l.split(',')

factors = {2: [1], 3: [1], 4: [1, 2], 5: [1], 6: [1, 2, 3], 7: [1], 8: [1, 2, 4], 9: [1, 3], 10: [1, 2, 5], 11: [1], 12: [1, 2, 3, 4, 6], 13: [1], 14: [1, 2, 7]}


def isValid(number: int):
    numString = str(number)
    length = len(numString)
    if length == 1:
        return False
    groupLengths = factors[length]
    for group in groupLengths:
        pattern = numString[:group]
        isValidPattern = True
        for i in range(0, length, group):
            if pattern != numString[i:i+group]:
                isValidPattern = False
                break
        if isValidPattern:
            return True
    return False

total = 0
for pair in pairs:
    nums = pair.split('-')
    start = int(nums[0])
    end = int(nums[1])
    for i in range(start, end+1):
        if isValid(i):
            total = total + i

print(total)