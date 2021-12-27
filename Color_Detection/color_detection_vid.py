import cv2
import numpy as np

class ColorPiker:
    def __init__(self):
        self.cam_id = 0
        self.frameWidth = 640
        self.frameHeight = 480

        self.cap = cv2.VideoCapture(self.cam_id, cv2.CAP_DSHOW)

        self.cap.set(3, self.frameWidth)
        self.cap.set(4, self.frameHeight)
        self.cap.set(10, 150)

        self.window_name = "COLOR HSV VALUES"
        self.default_hsv = {
            "Hue Min": [0, 179],
            "Hue Max": [179, 179],
            "Sat Min": [0, 255],
            "Sat Max": [255, 255],
            "Val Min": [0, 255],
            "Val Max": [255, 255],
            }

        self.selected_colors = []

    def _empty(self, a):
        pass

    def _trackbar(self):
        cv2.namedWindow(self.window_name)
        cv2.resizeWindow(self.window_name, 480, 320)

        for key in self.default_hsv.keys():
            cv2.createTrackbar(key, self.window_name, self.default_hsv[key][0], self.default_hsv[key][1], self._empty)
        
        return 0

    def pick(self):
        keys = list(self.default_hsv)
        self._trackbar()
        try:
            while True:
                success, img = self.cap.read()
                imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                h_min = cv2.getTrackbarPos(keys[0], self.window_name)
                h_max = cv2.getTrackbarPos(keys[1], self.window_name)
                s_min = cv2.getTrackbarPos(keys[2], self.window_name)
                s_max = cv2.getTrackbarPos(keys[3], self.window_name)
                v_min = cv2.getTrackbarPos(keys[4], self.window_name)
                v_max = cv2.getTrackbarPos(keys[5], self.window_name)

                lower_hsv = np.array([h_min, s_min, v_min])
                upper_hsv = np.array([h_max, s_max, v_max])

                imgMask = cv2.inRange(imgHSV, lower_hsv, upper_hsv)

                imgResult = cv2.bitwise_and(img, img, mask=imgMask)
                Mask2BGR = cv2.cvtColor(imgMask, cv2.COLOR_GRAY2BGR)

                try:
                    cv2.imshow(f"WebCam({self.cam_id}) original", img)
                    cv2.imshow(f"WebCam({self.cam_id}) Mask", Mask2BGR)
                    cv2.imshow(f"WebCam({self.cam_id}) Result", imgResult)
                    if cv2.waitKey(1) & 0xFF == ord('s'):
                        self.selected_colors.append([h_min, h_max, s_min, s_max, v_min, v_max])
                except:
                    print(f"No webcam is activate with id {self.cam_id}!")
                    break
        except:
            pass
        
        return self.selected_colors

""" FOR TESTING --> """
if __name__ == "__main__":
    colorPicker = ColorPiker()
    colorPicker.pick()
    print(colorPicker.selected_colors)