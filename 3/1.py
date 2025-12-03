f = open('./3/inp.txt', 'r')
def findBattery(batteries: str):
    maxI, maxV = 0, 0
    for i in range(len(batteries)-1):
        battery = int(batteries[i])
        if battery > maxV:
            maxV = battery
            maxI = i
    maxJ, maxVJ = 0, 0
    for j in range(maxI + 1, len(batteries)):
        battery = int(batteries[j])
        if battery > maxVJ:
            maxJ = j
            maxVJ = battery
    return int(batteries[maxI] + batteries[maxJ])
total = 0
for l in f:
    total = total + findBattery(l.strip())
print(total)