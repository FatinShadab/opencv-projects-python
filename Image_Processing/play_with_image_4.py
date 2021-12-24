import cv2
import numpy as np



class ShapeDectector:
    def __init__(self, path):
        self.img = cv2.imread(path)
        self.result_img = self.img.copy()

    def get_canny(self):
        imGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # Here 1 is the sigma value higher the sigma value for 
        # more blur and (7, 7) is the kernel
        imBlur = cv2.GaussianBlur(imGray, (7, 7), 1)
        imCanny = cv2.Canny(imBlur, 50, 50)

        return imCanny

    def get_contours(self):
        contours, hierarchy = cv2.findContours(self.get_canny(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return contours

    def get_objtype(self, objcor, perams):
        x, y, w, h = perams
        if objcor == 3:
            objType = "Tri"
        elif objcor == 4:
            aspRatio = w/float(h)
            if aspRatio > .95 and aspRatio < 1.05: 
                objType = "Squre"
            else:
                objType = "Rectangle"
        elif objcor == 5:
            objType = "Pentagon"
        elif objcor == 6:
            objType = "Hexagon"
        elif objcor > 6:
            objType = "Circle"
        else:
            objType = "!"

        return objType

    def dectect(self):
        for cnt in self.get_contours():
            area = cv2.contourArea(cnt)
            if area > 500:
                cv2.drawContours(self.result_img, cnt, -1, (255, 0, 0), 3)
                peri = cv2.arcLength(cnt, True) 
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                objCorner = len(approx)
                x, y, w, h = cv2.boundingRect(approx)

                cv2.putText(self.result_img, self.get_objtype(objCorner, (x, y, w, h)), 
                    (x+(w//2)-10, y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0), 1)

        cv2.imshow("Original Image", self.img)
        cv2.imshow("Result Image", self.result_img)
        cv2.waitKey(0)

        return 0
    

if __name__ == "__main__":
    path = "F:/git/opencv-projects-python/resources/shapes.png"
    detector = ShapeDectector(path)
    detector.dectect()