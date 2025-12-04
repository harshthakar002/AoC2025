f = open('./4/inp.txt', 'r')
lines = f.readlines()
matrix = []
for line in lines:
    line = line.strip()
    matrix.append(list(line))
def hasLessThan4Neighbours(matrix, i, j):
    neighbourCount = 0
    m = len(matrix)
    n = len(matrix[0])
    if i > 0:
        if matrix[i-1][j] == '@':
            neighbourCount += 1
        if j > 0:
            if matrix[i-1][j-1] == '@':
                neighbourCount += 1
        if j < n - 1:
            if matrix[i-1][j+1] == '@':
                neighbourCount += 1
    if j > 0:
        if matrix[i][j-1] == '@':
            neighbourCount += 1 
    if j < n - 1:
        if matrix[i][j+1] == '@':
            neighbourCount += 1
    if i < m - 1:
        if matrix[i+1][j] == '@':
            neighbourCount += 1
        if j > 0:
            if matrix[i+1][j-1] == '@':
                neighbourCount += 1
        if j < n - 1:
            if matrix[i+1][j+1] == '@':
                neighbourCount += 1
    return neighbourCount < 4
def moveRolls(mat):
    m = len(matrix)
    n = len(matrix[0])
    rollsToMove = []
    for i in range(m):
        for j in range(n):
            if mat[i][j] != '@':
                continue
            if hasLessThan4Neighbours(mat, i, j):
                rollsToMove.append((i, j))
    for i, j in rollsToMove:
        mat[i][j] = 'x'
    return len(rollsToMove)

rollsToMove = moveRolls(matrix)
print(rollsToMove)
                