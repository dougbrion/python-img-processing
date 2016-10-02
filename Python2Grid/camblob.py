from PIL import Image
from SimpleCV import Camera
import numpy
import scipy
# Initialize the camera
cam = Camera()
# Loop to continuously get images

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

while True:

    # Get Image from camera
    im = cam.getImage()
        # Show the image
    for y in range(0,480):
        for x in range(0, 640):
            (r, g, b) = im[x, y]

            if pixColour(r, g, b) == 1:
                r = 255
                b = 0
                g = 0
            elif pixColour(r, g, b) == 2:
                r = 0
                b = 0
                g = 255
            elif pixColour(r, g, b) == 3:
                r = 0
                b = 255
                g = 0
            elif pixColour(r, g, b) == 4:
                r = 255
                b = 0
                g = 255
            elif pixColour(r, g, b) == 5:
                r = 0
                b = 0
                g = 0

            im[x, y] = (r, g, b)



    im.show()
