from PIL import Image
from collections import namedtuple
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

RedString = namedtuple('RedStart', 'RedFinish')
RedStringList = []

for y in range(0, img.size[1]):
    curRedString = (-1, -1)
    for x in range(0, img.size[0]):
        (r, g, b) = pixels[x][y]
        if pixColour(r, g, b) != 1:
            if curRedString.RedFinish < 0 and curRedString.RedStart > 0:
                curRedString.RedFinish = x
                curRedString = (-1, -1)


img.save("data.jpg")
