f = open('./1/inp.txt', 'r')
instructions = f.readlines()
def transform( number, instruction: str):
    isPlus = instruction[0] == 'R'
    mul = 1
    if not isPlus:
        mul = -1
    add = int(instruction[1:])
    return (number + (mul * add))
start = 50
count = 0
scount = 0
for instruction in instructions:
    newStart = transform(start, instruction)
    if newStart >= 100:
        count += abs(newStart // 100)
    if (newStart <= 0):
        if start != 0:
            count += (abs(newStart) // 100) + 1
        else:
            count += (abs(newStart) // 100)
    start = newStart % 100
print(count)