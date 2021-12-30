import numpy as np
import cv2
from matplotlib import pyplot as plt
  
  
# read the image
img = cv2.imread('images.png')
#img = cv2.resize(img, (960, 540))
  
# convert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# detect corners with the goodFeaturesToTrack function.
corners = cv2.goodFeaturesToTrack(gray, 13, 0.01, 10)
corners = np.int0(corners)
  
# we iterate through each corner, 
# making a circle at each point that we think is a corner.
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)
  
plt.imshow(img), plt.show()