import cv2
import numpy as np

class ImgRC:
    def __init__(self, path):
        self.image = cv2.imread(path)

    def resize(self, width, hight):
        resized_img = cv2.resize(self.image, (width, hight))
        cv2.imshow(f"resized ({width}x{hight})p", resized_img)
        cv2.waitKey(0)
        return 0

    def crop(self, hight, width):
        cropped = self.image[hight[0]:hight[1], width[0]:width[1]]
        cv2.imshow(f"Cropped Image", cropped)
        cv2.waitKey(0)
        return 0

if __name__ == "__main__":
    # initialize the class
    image = ImgRC("F:/git/opencv-projects-python/resources/nature.jpg")
    #----------------
    #To Show Original Image
    #cv2.imshow("Original Image", image.image)
    #cv2.waitKey(0)
    #-----------------

    #---------------
    # Original Image sape
    #print(image.image.shape)
    #---------------

    #---------------
    # pass the width and hight
    #
    #image.resize(1200, 700)
    #---------------

    #---------------
    # pass 2 hight value(start, end) in a list and 2 width value(start, end) in a list
    #
    #image.crop([0,150], [150,300])
    #---------------
