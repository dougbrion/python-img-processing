# Douglas Brion

# Import libraries needed for the project
from scipy import *
from scipy import signal
from PIL import Image
import scipy.misc
import math

# The image that you want to use the Laplacian operator on
usedImage = 'moon.jpeg'

# Open the desired JPEG image as an array
img = array(Image.open(usedImage).convert("L"))

# Laplacian operator
kernel = [[-1, -1, -1],
           [-1, 8, -1],
           [-1, -1, -1]]

# CONVOLUTION 1
# Convolute the input image with the laplacian kernel
# Generate output array im of the convolution
im = signal.convolve(img, kernel, mode='same')

# Print array to console
print ('Im: Convolution 1')
print (im)

# Save the arrays created as JPEG images
scipy.misc.imsave('im.jpeg', im)

# Add the convoluted image to the original to start sharpen
final = im + img

# Save combined image
scipy.misc.imsave('final.jpeg', final)

print ('Finished Laplacian Operator')
