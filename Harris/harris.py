# Douglas Brion

# Import the necessary libraries
from scipy import *
from scipy import signal
from PIL import Image
from pylab import *
import scipy.misc
import matplotlib.pyplot as plt

# Image you want to test the corner detection on
usedImage = 'lena.jpeg'

# Open JPEG image as an array
img = array(Image.open(usedImage).convert("L"))

# Function for determining kernels for Harris Corner Detection
def generateKernels(size, sizeY=None):
    size = int(size)
    if not sizeY:
        sizeY = size
    else:
        sizeY = int(sizeY)
    y, x = mgrid[-size:size + 1, -sizeY:sizeY + 1]

    # Calculate Left-Right Kernel
    kernelX = - x * exp(-(x**2 / float((0.5 * size)**2)+y**2 / float((0.5 * sizeY)**2)))
    # Calculate Up-Down Kernel
    kernelY = - y * exp(-(x**2 / float((0.5 * size)**2)+y**2 / float((0.5 * sizeY)**2)))

    return kernelX, kernelY

# Basic Gaussian Blur Kernel
gauss = [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]]

# Call generateKernels function to make Harris kernels
kernelX, kernelY = generateKernels(1)

# Print to console arrays
print ('Kernel X:')
print (kernelX)
print ('Kernel Y:')
print (kernelY)

# CONVOLUTION 1
# Convolute the input image with the kernels generated separately
# Create output array of Left-Right convolution
imX = signal.convolve(img, kernelX, mode='same')
# Create output array of Up-Down convolution
imY = signal.convolve(img, kernelY, mode='same')

# Print arrays to console
print ('Im X: Convolution 1')
print (imX)
print ('Im Y: Convolution 1')
print (imY)

# Save the arrays generated as JPEGs
scipy.misc.imsave('imX.jpeg', imX)
scipy.misc.imsave('imY.jpeg', imY)

# CONVOLUTION 2
# Using the arrays from the previous convolution create new arrays by convoluting with Gaussian blur kernel
# Multiply the result of the previous Left-Right convolution with itself and then convolute with Gauss
Wxx = signal.convolve(imX*imX,gauss, mode='same')
# Multiply the result of the previous Left-Right convolution with the result of the Up-Down and then convolute with Gauss
Wxy = signal.convolve(imX*imY,gauss, mode='same')
# Multiply the result of the previous Up-Down convolution with itself and then convolute with Gauss
Wyy = signal.convolve(imY*imY,gauss, mode='same')

# Print arrays to console
print ('Wxx: Convolution 2')
print (Wxx)
print ('Wxy: Convolution 2')
print (Wxy)
print ('Wyy: Convolution 2')
print (Wyy)

# Save the arrays generated as JPEGs
scipy.misc.imsave('Wxx.jpeg', Wxx)
scipy.misc.imsave('Wxy.jpeg', Wxy)
scipy.misc.imsave('Wyy.jpeg', Wyy)

# Using the arrays generated for Wxx, Wxy and Wyy - compute the Determinant and Trace
# The Determinant array is the output Harris Corner detected image
Wdet = Wxx*Wyy - Wxy**2
Wtr = Wxx + Wyy

# Print arrays to console
print ('Wdet: Determinant')
print (Wdet)
print ('Wtr: Trace')
print (Wtr)

# Save the arrays generated as JPEGs
scipy.misc.imsave('Wdet.jpeg', Wdet)
scipy.misc.imsave('Wtr.jpeg', Wtr)

# Final Harris image is  Determinant / Trace
harrisImage = Wdet

# Threshold for eliminating noise
threshold = 0.5

# Minimum distance from picture edge
minDistance = 10

# Unravel the 2D array into a contiguous flattened 1D array
# Find the best corner candidates above a certain threshold
thresholdCorners = max(harrisImage.ravel()) * threshold
harrisThreshold = (harrisImage > thresholdCorners)

scipy.misc.imsave('harris.jpeg', harrisThreshold)

# Find coordinate candidates
candidates = harrisThreshold.nonzero()

# Create arrays of X coordinates, Y coordinates and both
xCoords = [(candidates[1][x]) for x in range(len(candidates[0]))]
yCoords = [(candidates[0][y]) for y in range(len(candidates[0]))]
coordinates = [(candidates[1][i],candidates[0][i]) for i in range(len(candidates[0]))]

# Array for the values of the different corner candidates
candidateVals = [harrisImage[i[1]][i[0]] for i in coordinates]
# Sort all the candidates
index = argsort(candidateVals)

# Output image with overlay plot of corners detected using PyPlot
outputImage = plt.imread(usedImage)
imPlot = plt.imshow(outputImage)
plt.scatter(x=xCoords, y=yCoords, color='yellow', s=120)  # s = size
plt.show()

print ('Finished plotting corners')
