f = open('./7/inp.txt', 'r')
matrix = []
for l in f.readlines():
    matrix.append(list(l.strip()))
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '.':
            matrix[i][j] = 0
        if matrix[i][j] == 'S':
            matrix[i][j] = 1

def printRow(row):
    s = ''
    for x in row:
        s += str(x)
    print(s)

def printMatrix(matrix):
    for row in matrix:
        printRow(row)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            matrix[i][j-1] += matrix[i-1][j]
            matrix[i][j+1] += matrix[i-1][j]
            matrix[i][j] = 0
            continue
        if i > 0:
            matrix[i][j] += matrix[i-1][j]

print(sum(matrix[-1]))