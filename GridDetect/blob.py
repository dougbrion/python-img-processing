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





img = Image.open("anglemarkers.jpg")

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
#Integer size of the marker (in pixels)
markerSizes = []
#Integer rotation of the marker from 0 to 15 clockwise
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

        # BLANK tile marker check RGRG
        if window[0][0] == 1 and window[2][2] == 1 and window[2][0] == 2 and window[0][2] == 2:
            print("RGRG 'Blank tile' Marker has been found at center (", x*6, ",", y*6, ") with rotation 0")
            for xmark in range((x-10) * 6, (x+10)*6):
                for ymark in range((y-10)*6, (y+10)*6):
                    pixels[xmark, ymark] = (0, 0, 0)    # We have found a BLANK tile marker
        elif window[1][0] == 2 and window[1][2] == 2 and window[0][1] == 1 and window[2][1] == 1:
            print("RGRG 'Blank tile' Marker has been found at center (", x*6, ",", y*6, ") with rotation 45")
            for xmark in range((x-10) * 6, (x+10)*6):
                for ymark in range((y-10)*6, (y+10)*6):
                    pixels[xmark, ymark] = (0, 0, 0)     # We have found a BLANK tile marker

        # AND gate tile marker check RBRB
        elif window[0][0] == 1 and window[2][2] == 1 and window[2][0] == 3 and window[0][2] == 3:
            print("RBRB 'And tile' Marker has been found at center (", x*6, ",", y*6, ") with rotation 0")
            for xmark in range((x-10) * 6, (x+10)*6):
                for ymark in range((y-10)*6, (y+10)*6):
                    pixels[xmark, ymark] = (0, 0, 0)     # We have found an AND gate tile marker
        elif window[1][0] == 3 and window[1][2] == 3 and window[0][1] == 1 and window[2][1] == 1:
            print("RBRB 'And tile' Marker has been found at center (", x*6, ",", y*6, ") with rotation 45")
            for xmark in range((x-10) * 6, (x+10)*6):
                for ymark in range((y-10)*6, (y+10)*6):
                    pixels[xmark, ymark] = (0, 0, 0)

        # OR gate tile marker check GBGB
        elif window[0][0] == 2 and window[2][2] == 2 and window[2][0] == 3 and window[0][2] == 3:
            print("GBGB 'Or tile' Marker has been found at center (", x*6, ",", y*6, ") with rotation 0")
            for xmark in range((x-10) * 6, (x+10)*6):
                for ymark in range((y-10)*6, (y+10)*6):
                    pixels[xmark, ymark] = (0, 0, 0)     # We have found an OR gate tile marker
        elif window[1][0] == 3 and window[1][2] == 3 and window[0][1] == 2 and window[2][1] == 2:
            print("GBGB 'Or tile' Marker has been found at center (", x*6, ",", y*6, ") with rotation 45")
            for xmark in range((x-10) * 6, (x+10)*6):
                for ymark in range((y-10)*6, (y+10)*6):
                    pixels[xmark, ymark] = (0, 0, 0)     # We have found an OR gate tile marker

        # NOT gate tile marker check YRBR
        elif window[0][0] == 4 and window[2][2] == 3 and window[2][0] == 1 and window[0][2] == 1:
            print("YRBR 'Not tile' Marker has been found at center (", x*6, ",", y*6, ") with rotation 0")
            for xmark in range((x-10) * 6, (x+10)*6):
                for ymark in range((y-10)*6, (y+10)*6):
                    pixels[xmark, ymark] = (0, 0, 0)      # We have found an NOT gate tile marker
        elif window[1][0] == 1 and window[1][2] == 1 and window[0][1] == 4 and window[2][1] == 3:
            print("YRBR 'Not tile' Marker has been found at center (", x*6, ",", y*6, ") with rotation 45")
            for xmark in range((x-10) * 6, (x+10)*6):
                for ymark in range((y-10)*6, (y+10)*6):
                    pixels[xmark, ymark] = (0, 0, 0)     # We have found an NOT gate tile marker

img.save("blobout.jpg")
