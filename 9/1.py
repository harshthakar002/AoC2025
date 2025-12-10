f = open('./9/inp.txt', 'r')
lines = f.readlines()
points = []
for line in lines:
    pstr = line.split(',')
    points.append((int(pstr[0]), int(pstr[1])))
maxArea = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1,y1 = points[i]
        x2,y2 = points[j]
        area = abs(x1-x2+1)*abs(y1-y2+1)
        maxArea = max(maxArea, area)
print(maxArea)