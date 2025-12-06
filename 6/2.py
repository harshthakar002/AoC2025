f = open('./6/inp.txt', 'r')
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
operations = []
for char in lines[len(lines)-1]:
    if char == '*' or char == '+':
        operations.append(char)
def transform(matrix):
    newMatrix = []
    m = len(matrix)
    n = 0
    for i in range(m):
        n = max(n, len(matrix[i]))
    for i in range(n):
        newMatrix.append('')
    for i in range(m):
        for j in range(len(matrix[i])):
            newMatrix[j] += matrix[i][j]
    return newMatrix
def getNumberList(matrix):
    numbers = [[]]
    n = 0
    for row in matrix:
        srow = row.strip()
        if srow == '':
            numbers.append([])
            n += 1
        else:
            numbers[n].append(int(row))
    return numbers
total = 0
numbers = getNumberList(transform(lines[:len(lines)-1]))
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