from a import buildLayers

def buildImage(layers):
    image = []

    for row in range(6):
        tempRow = []
        for col in range(25):
            tempCol = ''
            for layer in range((len(layers)-1), -1, -1):
                pixel = layers[layer][row][col]
                if pixel == 0: #black
                    tempCol = " "
                elif pixel == 1: #white
                    tempCol = "*"
            tempRow.insert(col, tempCol)

        image.insert(row, tempRow)

    printImage(image)

def printImage(img):
    for row in range(len(img)):
        for col in range(len(img[row])):
            print(img[row][col], end='')
        print('')

def main():
    buildImage(buildLayers())

if __name__ == "__main__":
    main()