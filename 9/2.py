f = open('./9/inp.txt', 'r')
lines = f.readlines()
points = []
for line in lines:
    pstr = line.split(',')
    points.append((int(pstr[1]), int(pstr[0])))
maxX, maxY = 0, 0
for point in points:
    x,y = point
    maxX = max(x, maxX)
    maxY = max(y, maxY)
maxX += 1
maxY += 1
matrix = []
for i in range(maxX):
    matrix.append([])
    for j in range(maxY):
        matrix[i].append('.')
print('Matrix Created')
for point in points:
    x, y = point
    matrix[x][y] = 'R'
for i in range(-1, len(points)-1):
    j = i + 1
    x1,y1 = points[i]
    x2,y2 = points[j]
    print(str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2))
    if y1 == y2:
        for k in range(min(x1,x2)+1, max(x1,x2)):
            matrix[k][y1] = 'G'
    if x1 == x2:
        for k in range(min(y1,y2)+1, max(y1,y2)):
            matrix[x1][k] = 'G'
def isInside(matrix, i, j):
    hasTop, hasBot, hasLeft, hasRight = False, False, False, False
    for m in range(i, -1, -1):
        if matrix[m][j] != '.':
            hasTop = True
            break
    for m in range(i, len(matrix)):
        if matrix[m][j] != '.':
            hasBot = True
            break
    for n in range(j, -1, -1):
        if matrix[i][n] != '.':
            hasLeft = True
            break
    for n in range(j, len(matrix[0])):
        if matrix[i][n] != '.':
            hasRight = True
            break
    return hasTop and hasBot and hasLeft and hasRight
for i in range(maxX):
    for j in range(maxY):
        if matrix[i][j] != '.':
            continue
        if isInside(matrix, i, j):
            matrix[i][j] = 'G'
for i in range(len(matrix)):
    print(''.join(matrix[i]))
def isValidRect(matrix, x1, y1, x2, y2):
    for i in range(min(x1, x2), max(x1,x2)):
        for j in range(min(y1, y2), max(y1,y2)):
            if matrix[i][j] == '.':
                return False
    return True
maxArea = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1,y1 = points[i]
        x2,y2 = points[j]
        if isValidRect(matrix, x1, y1, x2, y2):
            area = abs(x1-x2+1)*abs(y1-y2+1)
            maxArea = max(maxArea, area)
print(maxArea)
            