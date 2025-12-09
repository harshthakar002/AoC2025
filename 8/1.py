from math import sqrt
f = open('./8/inp.txt', 'r')
points = []
lines = f.readlines()
for line in lines:
    line = line.strip()
    pointStr = line.split(',')
    points.append((int(pointStr[0]), int(pointStr[1]), int(pointStr[2])))
graphs = []
for point in points:
    graphs.append([point])
distances = []
def getDistance(point1, point2):
    x1,y1,z1 = point1
    x2,y2,z2 = point2
    return sqrt(pow(x1-x2,2) + pow(y1-y2,2) + pow(z1-z2,2))
def merge(graphs, i, j):
    graphs[i] = graphs[i] + graphs[j]
    del graphs[j]
def gfind(graphs, point):
    x,y,z = point
    for i in range(len(graphs)):
        for gPoint in graphs[i]:
            gx,gy,gz = gPoint
            if x == gx and y == gy and z == gz:
                return i
    return -1
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        point1 = points[i]
        point2 = points[j]
        d = getDistance(point1, point2)
        distances.append((point1, point2, d))
distances.sort(key=lambda entity: entity[2])
numOfConnections = 0
i = 0
while numOfConnections < 1000:
    point1, point2, d = distances[i]
    index1 = gfind(graphs, point1)
    index2 = gfind(graphs, point2)
    if index1 != index2:
        merge(graphs, index1, index2)
    numOfConnections += 1
    i += 1
graphs.sort(reverse=True, key=lambda graph: len(graph))
print(len(graphs[0]) * len(graphs[1]) * len(graphs[2]))