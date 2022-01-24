import numpy as np
import cv2
import glob
from scipy import misc

path = glob.glob("D:\Folk Festival Live Music") #storing the location of all the images in variable path
imgs = [] #creating an empty list
for img in path: #running a loop to iterate through every image in the file
    pic = plt.imread(img) #reading the image using matplotlib
    imgs.append(pic) #adding the image to the list