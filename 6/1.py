f = open('./6/inp.txt', 'r')
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
operations = []
for char in lines[len(lines)-1]:
    if char == '*' or char == '+':
        operations.append(char)
def getNumberList(matrix):
    numbers = []
    for i in range(len(matrix)):
        j = 0
        numList = matrix[i].split(' ')
        for num in numList:
            if num == '':
                continue
            if len(numbers) == j:
                numbers.append([])
            numbers[j].append(int(num))
            j += 1
    return numbers
total = 0
numbers = getNumberList(lines[:len(lines)-1])
for i in range(len(operations)):
    operation = operations[i]
    if operation == '*':
        mul = 1
        for num in numbers[i]:
            mul = mul * num
        total = total + mul
    else:
        for num in numbers[i]:
            total = total + num
print(total)