from os import getcwd

def buildLayers():

    width = 25
    height = 6

    f = open(getcwd() + '/data/day8.txt')
    imgData = f.readline()
    f.close()

    layers = []

    dataItr = 0
    layerItr = 0

    while dataItr < len(imgData):
        tempLayer = []  

        for row in range(height):
            tempRow = []
            for col in range(width):
                tempRow.insert(col, int(imgData[dataItr]))
                dataItr += 1
            
            tempLayer.insert(row, tempRow)

        layers.insert(layerItr, tempLayer)
        layerItr += 1

    return layers

def main():
    layers = buildLayers()

    layerStats = []

    for layer in range(len(layers)):
        stat = 0
        for row in range(6):
            for col in range(25):
                if int(layers[layer][row][col]) == 0:
                    stat += 1

        layerStats.insert(layer, stat)
            
    layer = layerStats.index(min(layerStats))
    
    numOfOnes = 0
    numOfTwos = 0

    for row in range(6):
        for col in range(25):
            if layers[layer][row][col] == 1:
                numOfOnes += 1
            elif layers[layer][row][col] == 2:
                numOfTwos += 1

    print(numOfOnes, 'x', numOfTwos, '=', (numOfOnes*numOfTwos))

if __name__ == "__main__":
    main()