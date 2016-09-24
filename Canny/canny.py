# Douglas Brion

# Import libraries needed for the project
from scipy import *
from scipy import signal
from PIL import Image
import scipy.misc
import math

# The image that you want to use the Canny filter on
usedImage = 'lena.jpeg'

# Open the desired JPEG image as an array
img = array(Image.open(usedImage).convert("L"))

# Gaussian Blur kernel
kernel = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]

# CONVOLUTION 1
# Convolute the input image with the gaussian blur kernel
# Generate output array gaussian of the convolution
gaussian = signal.convolve(img, kernel, mode='same')

# Print array to console
print ('Im: Convolution 1')
print (gaussian)

# Save the arrays created as JPEG images
scipy.misc.imsave('smooth.jpeg', gaussian)

# Sobel X (horizontal) kernel
kernelX = [[-1, 0, 1],
           [-2, 0, 2],
           [-1, 0, 1]]

# Sobel Y (vertical) kernel
kernelY = [[-1, -2, -1],
           [0, 0, 0],
           [1, 2, 1]]

# Diagonal Sobel kernel (Kirsch)
kernelXY = [[0,1,2],
            [-1,0,1],
            [-2,-1,0]]

# Diagonal Sobel kernel (Kirsch)
kernelYX = [[-2,-1,0],
            [-1,0,1],
            [0,1,2]]

# CONVOLUTION 2
# Convolute the smoothed image with the horizontal and vertical sobel kernels
# Generate output array imX of horizontal convolution
imX = signal.convolve(gaussian, kernelX, mode='same')
# Generate output array imY of vertical convolution
imY = signal.convolve(gaussian, kernelY, mode='same')
# Generate output array imX of horizontal convolution
imXY = signal.convolve(gaussian, kernelXY, mode='same')
# Generate output array imY of vertical convolution
imYX = signal.convolve(gaussian, kernelYX, mode='same')

# Print arrays to console
print ('Im X: Convolution 2')
print (imX)
print ('Im Y: Convolution 2')
print (imY)
print ('Im XY: Convolution 2')
print (imXY)
print ('Im YX: Convolution 2')
print (imYX)

# Save the arrays created as JPEG images
scipy.misc.imsave('imX.jpeg', imX)
scipy.misc.imsave('imY.jpeg', imY)
scipy.misc.imsave('imXY.jpeg', imXY)
scipy.misc.imsave('imYX.jpeg', imYX)

# The horizontal and vertical gradient approximations are combined to give final gradient magnitude
imFinal = sqrt(imX*imX + imY*imY + imXY*imXY + imYX*imYX)

# Print the canny edge detected image array
print ('Im Final: Combining Gradient Approximations')
print (imFinal)

# Save the final edge detected array as a JPEG image
scipy.misc.imsave('canny.jpeg', imFinal)

print ('Finished Canny edge detection')
