import os
import common

fuelReq = 0

f = open(os.getcwd() + '/data/day1a.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break

    fuelReq += common.fuel_counter_upper(int(line))

f.close()

print(fuelReq)