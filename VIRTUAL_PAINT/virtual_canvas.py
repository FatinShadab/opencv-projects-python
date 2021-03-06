import cv2
import numpy as np


class VPaint:
    def __init__(self, camId, HSVCOLORS, BGRCOLORS):
        
        self.ID = camId 
        self.frameWidth = 640
        self.frameHeight = 480
        self.brightness = 150
        self.cam = cv2.VideoCapture(self.ID, cv2.CAP_DSHOW)

        self.cam.set(3, self.frameWidth)
        self.cam.set(4, self.frameHeight)
        self.cam.set(10, self.brightness)

        self.HSV_VALS = HSVCOLORS
        self.BGR_VALS = BGRCOLORS

        self.drawPoints = []

        self.ResultImg = None

    def _get_contours(self, SourceImg):
        contours, hierarchy = cv2.findContours(SourceImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        x, y, w, h = (0, 0, 0, 0)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                    peri = cv2.arcLength(cnt, True) 
                    approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                    x, y, w, h = cv2.boundingRect(approx)
        return (x+w//2, y)

    def _get_color_obj_pos(self, SourceImg):
        imgHSV = cv2.cvtColor(SourceImg, cv2.COLOR_BGR2HSV)
        for idx, val in enumerate(self.HSV_VALS):
            lower = np.array(val[0:3])
            upper = np.array([val[3:6]])
            mask = cv2.inRange(imgHSV, lower, upper)
            x, y = self._get_contours(mask)
            cv2.circle(self.ResultImg, (x, y), 10, self.BGR_VALS[idx], cv2.FILLED)
            if x != 0 and y != 0:
                self.drawPoints.append((x, y, idx))

    def _draw_on_canvas(self):
        for point in self.drawPoints:
            cv2.circle(self.ResultImg, (point[0], point[1]), 10, self.BGR_VALS[point[2]], cv2.FILLED)

    def open_canvas(self):
        while True:
            success, img = self.cam.read()
            self.ResultImg = img.copy()
            try:
                self._get_color_obj_pos(img)
                self._draw_on_canvas()
                cv2.imshow(f"WebCam({self.ID})", self.ResultImg)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("pressed q to exit !")
                    break
            except:
                print(f"No webcam is activate with id {self.ID}!")
                break


if __name__ == "__main__":
    myColors = [[5, 107, 0, 19, 255, 255]]
        
    myColors_BGR = [[0, 140, 255]]

    paint = VPaint(0, myColors, myColors_BGR)
    paint.open_canvas()