import math
import os

fuelReq = 0

def fuel_counter_upper(mass):
    return math.floor((mass / 3)) - 2

f = open(os.getcwd() + '/data/day1a.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break

    fuelReq += fuel_counter_upper(int(line))

f.close()

print(fuelReq)