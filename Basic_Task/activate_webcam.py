"""
Basic II : How to use webcam by opencv ?

i) if have one web cam connected than pass 0(id) to the 'cv2.VideoCapture' func
and cv2.CAP_DSHOW (only for windows platform)

ii) use .set method of the cam object with id:3 and int:value for width of output window
iii) use .set method of the cam object with id:4 and int:value for hight of output window
iv) use .set method of the cam object with id:10 and int:value for brightness lvl of cam video stream
"""


import cv2

def acticate_cam(cid, width=640, hight=480, brightness_lvl=100):

    cam = cv2.VideoCapture(cid, cv2.CAP_DSHOW) # add cv2.CAP_DSHOW only for windows to avoid warnning

    # WxH : (width x hight) p
    cam.set(3, width)
    cam.set(4, hight)
    cam.set(10, brightness_lvl)

    while True:
        success, img = cam.read()
        try:
            cv2.imshow(f"WebCam({cam_id})", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("pressed q to exit !")
                break
        except:
            print(f"No webcam is activate with id {cam_id}!")
            break
    return 0


if __name__ == "__main__":

    cam_id = 0
    acticate_cam(cam_id)