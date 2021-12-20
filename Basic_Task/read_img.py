"""
Basic I : How to read images ?

To hold or read a image we will use a image variable and 
we will need the 'imread'(which will take the img loc path) 
function to do so after that in order to show the image we 
will use 'imshow'(which will take output window name as a string 
and the image object from imread func) function. To make the window
stay we will use waitKey function with 0 which means infinity any 
other value will be in ms. 
"""


import cv2

def read_image(img_path):
    img = cv2.imread(img_path)
    cv2.imshow("Output", img)
    cv2.waitKey(0)
    return 0

if __name__ == "__main__":
    img_path = "F:/git/opencv-projects-python/resources/nature.jpg"
    read_image(img_path)