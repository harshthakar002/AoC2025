f = open('./2/inp.txt', 'r')
l = f.readline()
pairs = l.split(',')

def isValid(number: int):
    numString = str(number)
    length = len(numString)
    if length%2 != 0:
        return False
    return numString[:length//2] == numString[length//2:]

total = 0
for pair in pairs:
    nums = pair.split('-')
    start = int(nums[0])
    end = int(nums[1])
    for i in range(start, end+1):
        if isValid(i):
            total = total + i

print(total)
