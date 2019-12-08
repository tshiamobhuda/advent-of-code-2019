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
