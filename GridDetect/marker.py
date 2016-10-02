from PIL import Image
import math

# red = 0
# green = 1
# blue = 2
def pixColour(r, g, b):
    if r > 2*g and r > 2*b:
        return 0
    if g > 2*r and g > 2*b:
        return 1
    if b > 2*r and b > 2*g:
        return 2

img = Image.open("rbgtest.jpg")
print ("The size of the image is: ")
print (img.size)
pixels = img.load()


line1=[(0, 0, 0) for i in range(img.size[0])]
line2=[(0, 0, 0) for i in range(img.size[0])]
line3=[(0, 0, 0) for i in range(img.size[0])]
line4=[(0, 0, 0) for i in range(img.size[0])]
line5=[(0, 0, 0) for i in range(img.size[0])]

for y in range(0, img.size[1]):
    line5 = line4
    line4 = line3
    line3 = line2
    line2 = line1

    curRed = 0;
    for x in range(0, img.size[0]):
        line1[x]=pixels[x,y]

        (r1, g1, b1) = line1[x]
        (r2, g2, b2) = line2[x]
        (r3, g3, b3) = line3[x]
        (r4, g4, b4) = line4[x]
        (r5, g5, b5) = line5[x]

        if pixColour(r1, g1, g1) == 0 and pixColour(r2, g2, g2) == 0 and pixColour(r3, g3, g3) == 0 and pixColour(r4, g4, g4) == 0 and pixColour(r5, g5, g5) == 0:
            curRed = curRed + 1
img.save("outputMarker.jpg")
