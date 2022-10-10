import sys
def inputData():
    infile = sys.stdin
    formattingData = [line.replace("\n", "").split(" ") for line in infile]
    users = formattingData[0][0]
    data = formattingData[0][1]
    id = formattingData[0][2]
    infectedList = []
    infectedList.append(id)
    index = 1

    while True:
        if "".join(formattingData[index]) == "000":
            print(len(infectedList))
            break

        if len(formattingData[index]) == 3:
            print(len(infectedList))
            users = formattingData[index][0]
            data = formattingData[index][1]
            id = formattingData[index][2]
            infectedList = []
            infectedList.append(id)
            index += 1
            continue

        if ((formattingData[index][0] in infectedList and formattingData[index][1] not in infectedList) or 
        (formattingData[index][1] in infectedList and formattingData[index][0] not in infectedList)):
            infectedList.append(formattingData[index][1])
        index += 1
        
inputData()