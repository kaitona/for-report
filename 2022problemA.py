import sys

def inputData():
    data = sys.stdin
    line_counter = 0
    for line in data:
        if line_counter%2 == 0:
            days = int(line.replace("\n", ""))
        else:
            infectedList = line.replace("\n", "").split(" ")
            print(peakCount(days, infectedList))
        line_counter += 1

def peakCount(days, infectedList):
    count = 0
    for i in range(1,days-1):
        if (infectedList[i] > infectedList[i-1]) and  (infectedList[i] > infectedList[i+1]): count+= 1
    return count

inputData()

