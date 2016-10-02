from PIL import Image
import math

# red = 1
# green = 2
# blue = 3
# yellow = 4
# other = 5

def pixColour(r, g, b):
    if r > 2*g and r > 2*b:
        return 1
    elif g > 2*r and g > 2*b:
        return 2
    elif b > 2*r and b > 2*g:
        return 3
    elif r > 2*b and g > 2*b:
        return 4
    else:
        return 5

img = Image.open("rbgtest.jpg")

print ("The size of the image is: ")
print (img.size)

pixels = img.load()

line1=[(0, 0, 0) for i in range(img.size[0])]
line2=[(0, 0, 0) for i in range(img.size[0])]
line3=[(0, 0, 0) for i in range(img.size[0])]
line4=[(0, 0, 0) for i in range(img.size[0])]
line5=[(0, 0, 0) for i in range(img.size[0])]

num = 0
for y in range(0, img.size[0]):
    for x in range(0, img.size[1]):
        (r, g, b) = pixels[x, y]

        if pixColour(r, g, b) == 1:
            r = 255
            b = 0
            g = 0

            line1[num] = 1
            num = num + 1
        elif pixColour(r, g, b) == 2:
            r = 0
            b = 0
            g = 255

            line1[num] = 2
            num = num + 1
        elif pixColour(r, g, b) == 3:
            r = 0
            b = 255
            g = 0

            line1[num] = 3
            num = num + 1
        elif pixColour(r, g, b) == 4:
            r = 255
            b = 0
            g = 255

            line1[num] = 4
            num = num + 1
        elif pixColour(r, g, b) == 5:
            r = 0
            b = 0
            g = 0

            line1[num] = 5
            num = 0

        pixels[x, y] = (r, g, b)


img.save("output.jpg")
