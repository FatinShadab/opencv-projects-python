"""
In this script we learned --

    I) Run Function name 'shaped' to see:
        i) How to make image from np-array [Metrix]
        ii) How to make the image colorfull
        iii) How to draw shapes on the image [line, rectangle, circle] 
        
    II) Run Function name 'texted' to see:
        i) To write text/string in thye image
"""

import cv2
import numpy as np


def shaped():
    # uint8 = undefined int with 8 bits (0-255)
    img = np.zeros((512, 512, 3), np.uint8)

    # returns a tuple of image_hight, image_width, image_color_channel
    print(img.shape)

    # Turns the hole image in colored image with (B, G, R) values
    img[:] = 0, 0, 0

    # Draws a line in the image. 
    # The function takes img, (starting points(w, h)), (end points(w, h)), (line color(BGR values), line thikness)
    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

    # Draw a rectangle  in the image.
    # The function takes img, points of diagonal line of the rect(starting points(w, h)), (end points(w, h)), (line color(BGR values), line thikness)
    cv2.rectangle(img, (0, 0), (100, 100), (255, 0, 0), 5)

    # Draw a colored fill rectangle in the image.
    # The function takes img, points of diagonal line of the rect(starting points(w, h)), (end points(w, h)), (line color(BGR values), line thikness
    cv2.rectangle(img, (img.shape[1], img.shape[0]), (img.shape[1]-100, img.shape[0]-100), (255, 0, 0), cv2.FILLED)

    # Draw a circle
    # The function takes img, center points (w, h), radius of cicrcle, color(BGR values), thikness
    cv2.circle(img, (100, 450), 35, (0, 0, 255), 7)

    cv2.imshow("NP Image", img)
    cv2.waitKey(0)

    return 0

def texted():
    # uint8 = undefined int with 8 bits (0-255)
    img = np.zeros((512, 512, 3), np.uint8)

    # Put a text in a certain pos of img
    # The function takes img, text as string, pos(w, h), font, scale, color(BGR value), thikness
    cv2.putText(img, "Hello World !", (250, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)


    cv2.imshow("NP Image", img)
    cv2.waitKey(0)

    return 0


if __name__ == "__main__":
    #shaped()
    texted()
