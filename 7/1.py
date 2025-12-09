f = open('./7/inp.txt', 'r')
matrix = []
for l in f.readlines():
    matrix.append(list(l.strip()))
splitCount = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'S':
            matrix[i][j] = '|'
            continue
        if matrix[i][j] == '^':
            if matrix[i-1][j] == '.':
                continue
            hasSplit = False
            if matrix[i][j-1] == '.':
                matrix[i][j-1] = '|'
                hasSplit = True
            if matrix[i][j+1] == '.':
                matrix[i][j+1] = '|'
                hasSplit = True
            if hasSplit:
                splitCount += 1
        if matrix[i][j] == '.' and i > 0 and matrix[i-1][j] == '|':
            matrix[i][j] = '|'
print(splitCount)