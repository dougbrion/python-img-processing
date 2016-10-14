from SimpleCV import Camera
# Initialize the camera
cam = Camera()
# Loop to continuously get images
while True:
    # Get Image from camera
    img = cam.getImage()

    # Show the image
    img.show()
