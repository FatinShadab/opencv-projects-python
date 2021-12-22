"""
*** Problem/Task -- color detection from image
SOLVE:

    I) Read target image

    II) Turn target image to HSV (BGR2HSV)

    III) Build a TrackBar to get (H: Hue, S: Sat, V: value) positions
        *** (H_max, S_max, V_max, H_min, S_min, V_min)

    IV) Create A mask from the HSV Image and the HSV values
        *** from 6 positions values create 2 np-arrays one with lower 
        positions values and one with upper positions  

    v) Create the Output Image with the original image and the mask from step (IV)
"""


import cv2
import numpy as np


class ColorDetection:
    def __init__(self, path):
        self.path = path
        self.tracks = {
            "Hue Min": [0, 179],
            "Hue Max": [179, 179],
            "Sat Min": [0, 255],
            "Sat Max": [255, 255],
            "Val Min": [0, 255],
            "Val Max": [255, 255],
            }

    def _empty(self, a):
        pass

    def _trackbar(self):
        cv2.namedWindow("TrackBars")
        cv2.resizeWindow("TrackBars", 640, 240)

        for key in self.tracks.keys():
            cv2.createTrackbar(key, 'TrackBars', self.tracks[key][0], self.tracks[key][1], self._empty)
        
        return 0

    def detect_color_obj(self, show_all=False):
        self._trackbar()
        keys = list(self.tracks)
        try:
            while True:
                img = cv2.imread(self.path)
                imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                # Get all the TrackBar Pos
                h_min = cv2.getTrackbarPos(keys[0], "TrackBars")
                h_max = cv2.getTrackbarPos(keys[1], "TrackBars")
                s_min = cv2.getTrackbarPos(keys[2], "TrackBars")
                s_max = cv2.getTrackbarPos(keys[3], "TrackBars")
                v_min = cv2.getTrackbarPos(keys[4], "TrackBars")
                v_max = cv2.getTrackbarPos(keys[5], "TrackBars")

                # Create a mask
                lower = np.array([h_min, s_min, v_min])
                upper = np.array([h_max, s_max, v_max])

                mask = cv2.inRange(imgHSV, lower, upper)

                # Create a image with target object
                imgResult = cv2.bitwise_and(img, img, mask=mask)

                # show all
                cv2.imshow("Result Image", imgResult)
                if show_all:
                    cv2.imshow("Original Image", img)
                    cv2.imshow("HSV Image", imgHSV)
                    cv2.imshow("HSV MASK Image", mask)

                cv2.waitKey(1)
        except:
            print("Trackbar Closed!")

        return 0




if __name__ == "__main__":
    path = "F:/git/opencv-projects-python/resources/stars.jpg"
    cd = ColorDetection(path)
    cd.detect_color_obj()