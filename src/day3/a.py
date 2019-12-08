import os
import common

lines = []
paths = []
sumOfIntersections = []

f = open(os.getcwd() + '/data/day3.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    
    lines.append(line)

f.close()

for line in lines:
    paths.append(common.buildLinePath(line.split(',')))

intersections = set(paths[0]).intersection(paths[1])

for points in intersections:
    sumOfIntersections.append(abs(points[0]) + abs(points[1]))

sumOfIntersections.sort()

print(min(sumOfIntersections[1::])) if 0 in sumOfIntersections else print(min(sumOfIntersections))