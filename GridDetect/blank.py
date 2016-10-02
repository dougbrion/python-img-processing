from PIL import Image
import math
import pickle


# Pixel Colour check function
def pixColour(r, g, b):
    if r > 2*g and r > 2*b:
        return 1                    # Pixel is mostly red
    elif g > 2*r and g > 2*b:
        return 2                    # Pixel is mostly green
    elif b > 2*r and b > 2*g:
        return 3                    # Pixel is mostly blue
    elif r > 2*b and g > 2*b:
        return 4                    # Pixel is mostly yellow
    else:
        return 5                    # Pixel is mostly other





img = Image.open("grid.jpg")

print ("The size of the image is: ")
print (img.size)

pixels = img.load()

numRed = 0
numGreen = 0
numBlue = 0
numYellow = 0

#Creates a new grid for storing the sample information. This is 1/6th the size of the image
SampleGrid = [[0 for i in range(0, math.ceil(img.size[1]/6))] for i in range(0, math.ceil(img.size[0]/6))]

#Step through by 6 each time, this ignores a significant part of the image, 'Sampling' the colours at most areas
for y in range(0, img.size[1]-2, 6):
    for x in range(0, img.size[0]-2, 6):
        for i in range(x, x+4):
            for j in range(y, y+4):
                (r, g, b) = pixels[i, j]

                if pixColour(r, g, b) == 1:
                    r = 255
                    b = 0
                    g = 0
                    numRed = numRed + 1
                elif pixColour(r, g, b) == 2:
                    r = 0
                    b = 0
                    g = 255
                    numGreen = numGreen + 1
                elif pixColour(r, g, b) == 3:
                    r = 0
                    b = 255
                    g = 0
                    numBlue = numBlue + 1
                elif pixColour(r, g, b) == 4:
                    r = 255
                    b = 0
                    g = 255
                    numYellow = numYellow + 1
                elif pixColour(r, g, b) == 5:
                    r = 0
                    b = 0
                    g = 0

        if numRed > 5:
            #print ("found a block of red")
            for k in range(x, x+2):
                for l in range(y, y+2):
                    pixels[k, l] = (255, 0, 255)
            numRed = 0
            SampleGrid[math.ceil(x/6)][math.ceil(y/6)] = 1
        elif numGreen > 5:
            #print ("found a block of green")
            for k in range(x, x+2):
                for l in range(y, y+2):
                    pixels[k, l] = (0, 100,0)
            numGreen = 0
            SampleGrid[math.ceil(x/6)][math.ceil(y/6)] = 2
        elif numBlue > 5:
            #print ("found a block of blue")
            for k in range(x, x+2):
                for l in range(y, y+2):
                    pixels[k, l] = (0, 255,255)
            numBlue = 0
            SampleGrid[math.ceil(x/6)][math.ceil(y/6)] = 3
        elif numYellow > 5:
            #print ("found a block of yellow")
            for k in range(x, x+2):
                for l in range(y, y+2):
                    pixels[k, l] = (255, 165, 0)
            numYellow = 0
            SampleGrid[math.ceil(x/6)][math.ceil(y/6)] = 4
        else:
            for k in range(x, x+2):
                for l in range(y, y+2):
                    pixels[k, l] = (150, 150, 150)
            SampleGrid[math.ceil(x/6)][math.ceil(y/6)] = 0


    #etc....
    numRed = 0
    numGreen = 0
    numBlue = 0
    numYellow = 0

print(SampleGrid)

#String of the form WXYZ of the marker:
#    W X
#    Z Y
markerCodes = []
#Tuple of a tuple coordinates of the corners of the marker
markerCoords = []
#Integer size of the marker (in pixels)
markerRots = []

#Iterate through the Sample Grid, looking for markers
for y in range(0, math.ceil(img.size[1]/6) - 4):
    for x in range(0, math.ceil(img.size[0]/6) - 4):
        #5x5 window of sample blocks to check for a marker
        window = [
        [SampleGrid[x][y], SampleGrid[x+1][y], SampleGrid[x+2][y]],
        [SampleGrid[x][y+1], SampleGrid[x+1][y+1], SampleGrid[x+2][y+1]],
        [SampleGrid[x][y+2], SampleGrid[x+1][y+2], SampleGrid[x+2][y+2]]
        ]
        #testWindow2 = [[SampleGrid[x][y],SampleGrid[x+2][y]],[SampleGrid[x][y+2],SampleGrid[x+2][y+2]]]
        #testWindow3 = [[SampleGrid[x][y],SampleGrid[x+2][y]],[SampleGrid[x][y+1],SampleGrid[x+2][y+1]]]
        #testWindow4 = [[SampleGrid[x][y],SampleGrid[x+1][y]],[SampleGrid[x][y+2],SampleGrid[x+1][y+2]]]

        # BLANK tile marker check RGRG perpendicular
        if window[0][0] == 1 and window[2][2] == 1 and window[2][0] == 2 and window[0][2] == 2:
            markerCodes.append("RGRG")

            checkBlockTL = 1
            xCheckTL = x
            yCheckTL = y
            while checkBlockTL == 1:
                xCheckTL = xCheckTL - 1
                yCheckTL = yCheckTL - 1
                checkBlockTL = SampleGrid[xCheckTL][yCheckTL]
            #At this point, xCheckTL and yCheckTL give the coords of the first block that isn't red in the top left

            checkBlockTR = 2
            xCheckTR = x + 2
            yCheckTR = y
            while checkBlockTR == 2:
                xCheckTR = xCheckTR + 1
                yCheckTR = yCheckTR - 1
                checkBlockTR = SampleGrid[xCheckTR][yCheckTR]
            #At this point, xCheckTR and yCheckTR give the coords of the first block that isn't green in the top right

            checkBlockBR = 1
            xCheckBR = x + 2
            yCheckBR = y + 2
            while checkBlockBR == 1:
                xCheckBR = xCheckBR + 1
                yCheckBR = yCheckBR + 1
                checkBlockBR = SampleGrid[xCheckBR][yCheckBR]
            #At this point, xCheckBR and yCheckBR give the coords of the first block that isn't red in the bottom right

            checkBlockBL = 2
            xCheckBL = x
            yCheckBL = y + 2
            while checkBlockBL == 2:
                xCheckBL = xCheckBL - 1
                yCheckBL = yCheckBL + 1
                checkBlockBL = SampleGrid[xCheckBL][yCheckBL]
            #At this point, xCheckBL and yCheckBL give the coords of the first block that isn't green in the bottom left


            markerCoords.append((
            ((xCheckTL + 1)*6, (yCheckTL + 1)*6),
            ((xCheckTR - 1)*6, (yCheckTR + 1)*6),
            ((xCheckBR - 1)*6, (yCheckBR - 1)*6),
            ((xCheckBL + 1)*6, (yCheckBL - 1)*6)
            ))


for i in range(0, len(markerCodes)-1):
    ((xTL, yTL), (xTR, yTR), (xBR, yBR), (xBL, yBL)) = markerCoords[i]
    for yn in range(yTL, yBL):
        for xn in range(xTL, xTR):
            (r, g, b) = pixels[xn, yn]
            pixels[xn, yn] = (r/2, g/2, b/2)
    print(markerCodes[i], " marker has been found at TL(", xTL, ",", yTL, ") and TR(", xTR, ",", yTR, ") and BR(", xBR, ",", yBR, ") and BL(", xBL, ",", yBL, ")")

img.save("blankout.jpg")
