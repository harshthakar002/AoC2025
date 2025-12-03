f = open('./3/inp.txt', 'r')
def findBattery(batteries: str, length: int):
    if length == 0:
        return ''
    maxI, maxV = 0, 0
    for i in range(len(batteries)-length+1):
        battery = int(batteries[i])
        if battery > maxV:
            maxV = battery
            maxI = i
    return batteries[maxI] + findBattery(batteries[maxI+1:], length - 1)
total = 0
for l in f:
    total = total + int(findBattery(l.strip(), 12))
print(total)