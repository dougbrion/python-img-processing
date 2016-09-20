# Douglas Brion

# Import libraries needed for the project
from scipy import *
from scipy import signal
from PIL import Image
import scipy.misc
import math

# The image that you want to use the Gaussian Blur filter on
usedImage = 'lena.jpeg'

# Open the desired JPEG image as an array
img = array(Image.open(usedImage).convert("L"))

# Gaussian Blur kernel
kernel = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]

# CONVOLUTION 1
# Convolute the input image with the gaussian blur kernel
# Generate output array im of the convolution
im = signal.convolve(img, kernel, mode='same')

# Print array to console
print ('Im: Convolution 1')
print (im)

# Save the arrays created as JPEG images
scipy.misc.imsave('im.jpeg', im)

print ('Finished Sobel edge detection')
