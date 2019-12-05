import os

f = open(os.getcwd() + '/data/day2.txt')
intCode = f.readline()
f.close()

intCodeList = intCode.split(',')
index = 0

while True:
    opcode = intCodeList[index]
    if int(opcode) == 99:
        break

    val1Index = int(intCodeList[index+1])
    val2Index = int(intCodeList[index+2])
    val1 = int(intCodeList[val1Index])
    val2 = int(intCodeList[val2Index])

    if int(opcode) == 1:
        temp = val1 + val2
        storagePosition = int(intCodeList[index+3])
        intCodeList[storagePosition] = temp
    elif int(opcode) == 2:
        temp = val1 * val2
        storagePosition = int(intCodeList[index+3])
        intCodeList[storagePosition] = temp

    index += 4

print(intCodeList)
