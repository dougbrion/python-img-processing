# Douglas Brion

# Import libraries needed for the project
from PIL import Image
from scipy import *
import math

# The image that you want to use the Sobel filter on
usedImage = 'lena.jpeg'

# Open the desired JPEG image as an array
img = array(Image.open(usedImage).convert("L"))

# Sobel X (horizontal) kernel
xMatrix = [[-1, 0, 1],
           [-2, 0, 2],
           [-1, 0, 1]]

# Sobel Y (vertical) kernel
yMatrix = [[-1, -2, -1],
           [0, 0, 0],
           [1, 2, 1]]
