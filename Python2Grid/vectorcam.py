import scipy as sp
import scipy.ndimage as spimg
import matplotlib.pyplot as plt
from SimpleCV import Camera
from PIL import Image, ImageTk
import Tkinter

def newIMG(im):
    img = im.getNumpy()
    w, h = img.shape[0:2]
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]

    new_img = sp.zeros((w, h, 3), dtype='uint8')
    new_img[sp.logical_and(r > 3 * g, r > 3 * b)] = 255, 0, 0
    new_img[sp.logical_and(g > 3 * r, g > 3 * b)] = 0, 255, 0
    new_img[sp.logical_and(b > 3 * r, b > 3 * g)] = 0, 0, 255
    outputRed = sp.resize(sp.logical_and(r > 3 * g, r > 3 * b), (16, 12))
    outputGreen = sp.resize(sp.logical_and(g > 3 * r, g > 3 * b), (16, 12))
    outputBlue = sp.resize(sp.logical_and(b > 3 * r, b > 3 * g), (16, 12))

    print outputRed
    print outputGreen
    print outputBlue
    return new_img

def update_img():
    global tkimage

    im = cam.getImage()
    im.show()
    new_img = newIMG(im)

    new_img = sp.rot90(new_img, 3)
    new_img = sp.fliplr(new_img)
    disp = Image.fromarray(new_img, "RGB")
    #disp = Image.fromarray(output, "RGB")
    tkimage = ImageTk.PhotoImage(disp)
    label.config(image = tkimage)
    label.after(1, update_img)

cam = Camera()
im = cam.getImage()
root = Tkinter.Tk()

new_img = newIMG(im)

disp = Image.fromarray(new_img, "RGB")

tkimage = ImageTk.PhotoImage(disp)
label = Tkinter.Label(root, image=tkimage)
print "Loaded"
label.pack()
root.after(1, update_img)

root.mainloop()
