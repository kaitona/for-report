import sys
def inputData():
    infile = sys.stdin
    index = 0
    for data in infile:
        if index % 2 == 0:
            dataCount = int(data.replace("\n", ""))
            if dataCount <= 0: break
        else:
            salaryList = data.replace("\n", "").split(" ")
            print(countUpper(salaryList, dataCount))
        index += 1

def countUpper(data, dataCount):
    result = 0
    salaryAvg = sumOfList(data)/dataCount
    for salary in data:
        if int(salary) <= salaryAvg: result += 1
    return result

def sumOfList(data):
    result = 0
    for num in data:
        result += int(num)
    return result

inputData()
