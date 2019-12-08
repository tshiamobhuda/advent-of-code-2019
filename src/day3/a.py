import os

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

def buildLinePath(line):
    path = []
    x = 0
    y = 0

    for coordinate in line:    
        direction = coordinate[0]
        move = int(coordinate[1::])

        if direction == 'R':
            for i in range(x, (x+move)):
                path.append((i, y))
            x += move

        elif direction == 'L':
            for i in range(x, (x-move), -1):
                path.append((i, y))
            x -= move

        elif direction == 'U':
            for i in range(y, (y+move)):
                path.append((x, i))
            y += move

        elif direction == 'D':
            for i in range(y, (y-move), -1):
                path.append((x, i))
            y -= move
    else:
        path.append((x, y))

    return path

for line in lines:
    paths.append(buildLinePath(line.split(',')))

intersections = set(paths[0]).intersection(paths[1])

for points in intersections:
    sumOfIntersections.append(abs(points[0]) + abs(points[1]))

sumOfIntersections.sort()

print(min(sumOfIntersections[1::])) if 0 in sumOfIntersections else print(min(sumOfIntersections))