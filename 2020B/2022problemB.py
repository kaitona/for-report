import sys
def inputData():
    infile = sys.stdin
    formattingData = [line.replace("\n", "").split(" ") for line in infile]
    users = 0
    data = 0
    id = 0
    index = 0

    while True:
        if "".join(formattingData[index]) == "000":
            print("end")
            break
        if len(formattingData[index]) == 3:
            users = formattingData[index][0]
            data = formattingData[index][1]
            id = formattingData[index][2]
            print(users, data, id)
        index += 1
        
inputData()