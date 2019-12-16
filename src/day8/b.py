from a import buildLayers

def buildFinalImage(layers):
    
    finalImage = []
    
    for layer in range((len(layers)-1), -1, -1):
        tempLayer = []  

        for row in range(len(layers[layer])):
            tempRow = []
            for col in range(len(layers[layer][row])):
                tempRow.insert(col, layers[layer][row][col])

            tempLayer.insert(row, tempRow)
        
        if len(finalImage) == 0:
            finalImage.extend(tempLayer)
        else:
            for row in range(len(tempLayer)):
                for col in range(len(tempLayer[row])):
                    pixel = tempLayer[row][col]

                    if pixel == 0: #black
                        finalImage[row][col] = " "
                    elif pixel == 1: #white
                        finalImage[row][col] = "*"

    printImage(finalImage)

def printImage(img):

    for row in range(len(img)):
        for col in range(len(img[row])):
            pixel = img[row][col]
            if pixel == 0: #black
                img[row][col] = " "
            elif pixel == 1: #white
                img[row][col] = "*"

    for row in range(len(img)):
        for col in range(len(img[row])):
            print(img[row][col], end='')
        print('')

def main():
    buildFinalImage(buildLayers())

if __name__ == "__main__":
    main()