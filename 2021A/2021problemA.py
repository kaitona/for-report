import sys
import math

def inputData():
    infile = sys.stdin
    dataList = [data.replace("\n", "").split(" ") for data in infile]
    for i in range(len(dataList)):
        for j in range(len(dataList[i])):
            dataList[i][j] = int(dataList[i][j])

    for data in dataList:
        if max(data) <= 0: break
        luckyMarbles(data)

def luckyMarbles(data):
    minMarbles = ListOfMin(data)
    for i in range(len(data)):
        if data[i] > 0 and i != minMarbles: data[i] -= data[minMarbles]    
    if isOneBowl(data):
        print(max(data))
    else: luckyMarbles(data)

def isOneBowl(data):
    count=0
    for i in range(len(data)):
        if data[i] > 0: count += 1
        if count > 1: return False
    
    return True

def ListOfMin(data):
    index = -1
    min = math.inf
    for i in range(len(data)):
        if data[i] > 0 and data[i] < min:
            min = data[i]
            index = i
    return index

inputData()