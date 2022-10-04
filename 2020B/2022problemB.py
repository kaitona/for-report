import sys
def inputData():
    data = sys.stdin
    formattingData = [line.replace("\n", "").split(" ") for line in data]
    print(formattingData)
    user = 0
    patient = 0
    id = 0
    index = 0

    while True:
        if "".join(formattingData[index]) == "000":
            print("end")
            break
        if len(formattingData[index]) == 3:
            user = formattingData[index][0]
            patient = formattingData[index][1]
            id = formattingData[index][2]
            print(user, patient, id)
        index += 1
        
inputData()