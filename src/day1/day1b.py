import os
import common

sumOfFuelReq = 0

f = open(os.getcwd() + '/data/day1a.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break

    moduleTotalFuel = 0
    fuelReq = common.fuel_counter_upper(int(line))
    moduleTotalFuel += fuelReq
    
    while fuelReq > 0:
        temp = common.fuel_counter_upper(fuelReq)
        if temp > 0:
            fuelReq = temp
            moduleTotalFuel += temp
        else:
            break

    sumOfFuelReq += moduleTotalFuel

f.close()

print(sumOfFuelReq)