import cv2
import numpy as np


class ImgPro:
    """The ImgPro class contains the useages of cvtColor, GaussianBlur, Canny, dilate, erode functions of cv2 lib"""
    def __init__(self, path):
        self.img = cv2.imread(path)
        self.kernel = np.ones((5, 5), np.uint8)

    def _turn_gray(self):
        """returns the gray-color img object"""
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def _turn_blur(self):
        """returns the blur img object"""
        return cv2.GaussianBlur(self._turn_gray(), (7, 7), 0)

    def _turn_canny(self):
        """returns the canny img object"""
        return cv2.Canny(self.img, 150, 200)

    def _turn_dialation(self):
        """returns the dialation img object"""
        return cv2.dilate(self._turn_canny(), self.kernel, iterations=1)

    def _turn_eroded(self):
        """returns the enroded img object"""
        return cv2.erode(self._turn_dialation(), self.kernel, iterations=1)

    def show_all(self):
        """Shows all the image versions including the original one"""
        cv2.imshow("Original Image", self.img)
        cv2.imshow("Gray Image", self._turn_gray())
        cv2.imshow("Blur Image", self._turn_blur())
        cv2.imshow("Canny Image", self._turn_canny())
        cv2.imshow("Dialation Image", self._turn_dialation())
        cv2.imshow("Eroded Image", self._turn_eroded())
        cv2.waitKey(0)

        return 0

if __name__ == "__main__":

    image = ImgPro("F:/git/opencv-projects-python/resources/nature.jpg")
    image.show_all()