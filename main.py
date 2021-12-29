import numpy as np
import cv2
import os
import winsound

def webcamp():

    cam = cv2.VideoCapture(0)

    while True:
         ret, frame_1 = cam.read()
         ret, frame_2 = cam.read()
         dif = cv2.absdiff(frame_1, frame_2)
         gray = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
         blur = cv2.GaussianBlur(gray, (5, 5), 0)
         _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
         dilated = cv2.dilate(thresh, None, iterations=3)
         contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
         #cv2.drawContours(frame_1, contours, -1, (0, 255, 0), 2)

         for c in contours:
             if cv2.contourArea(c) < 2000:
                 continue
             x, y, w, h = cv2.boundingRect(c)
             cv2.rectangle(frame_1, (x, y), (x+w, y+h), (250, 25, 50), 2)
             winsound.Beep(500, 200)
             print("moving")

         cv2.imshow('black_window', frame_1)

         if cv2.waitKey(10) == ord('q'):
            break
        # when everything is done, release the capture
    cam.release()
    cv2.destroyAllWindows()

    return None


# Read and show images
def img_show():
    img = cv2.imread('123.jpg', 0)
    r_img = cv2.resize(img, (int(img.shape[1]*3), int(img.shape[0]*3)))
    cv2.imshow("Turja", r_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return None
# Uses web cams
def vc():
    cap = cv2.VideoCapture(0)
    
    while True:
        # capture frame-by-frame
        ret, frame = cap.read()

        #Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == ord('q'):
            break
    # when everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    return None
# control over resolution
def resize_v():
    cap = cv2.VideoCapture(0)
    
    def make_1080():
        cap.set(3, 1920)
        cap.set(4, 1080)
    
    def make_720():
        cap.set(3, 1280)
        cap.set(4, 720)
    
    def make_480():
        cap.set(3, 640)
        cap.set(4, 480)
    
    def change_res(width, height):
        cap.set(3, width)
        cap.set(4, height)
        
    change_res(120, 280)
    while True:
        # capture frame-by-frame
        ret, frame_1 = cap.read()

        # Display the resulting frame
        cv2.imshow('frame', frame_1)
        if cv2.waitKey(10) == ord('q'):
            break
    # when everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    return None
# for scaleing the vedio size
def rescale_v():
    cap = cv2.VideoCapture(0)
    
    def rescale_frame(frame, percent=75):
        scale_percent = 75
        width = int(frame.shape[1]* scale_percent / 100)
        height = int(frame.shape[0]* scale_percent / 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        
    while True:

        ret, frame = cap.read()

        frame_1 = rescale_frame(frame, percent=10)
        cv2.imshow('frame_1', frame_1)

        frame_2 = rescale_frame(frame, percent=150)
        cv2.imshow('frame_2', frame_2)
        if cv2.waitKey(10) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return None
#Reacords vedios and saves them
def rec_v():
    filename = 'video.avi'
    frames_per_s = 24.0
    my_res = '480p'
    # Set the resolution for the video
    def change_res(cap, width, height):
        cap.set(3, width)
        cap.set(4, height)
    # Standard Video Dimensions sizes
    STD_DIMENSIONS = {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }

    def get_dims(cap, res):
        width, height = STD_DIMENSIONS["480p"] # default resolution
        if res in STD_DIMENSIONS:
            width, height = STD_DIMENSIONS[res]
        change_res(cap, width, height)
        return width, height


    VEDIO_TYPE = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    def get_vedio_type(filename):
        filename, ext = os.path.splitext(filename)
        if ext in VEDIO_TYPE:
            return VEDIO_TYPE[ext]
        return VEDIO_TYPE['avi']


    cap = cv2.VideoCapture(0)
    dims = get_dims(cap, my_res)
    vedio_type_cv2 = get_vedio_type(filename)

    out = cv2.VideoWriter(filename, vedio_type_cv2, frames_per_s, dims)

    while True:
        # capture frame-by-frame
        ret, frame = cap.read()
        out.write(frame)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == ord('q'):
            break
    # when everything is done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return None

def face_rec():

    face_casecade = cv2.CascadeClassifier('F://git//opencv-projects-python//esources//datahaarcascade_frontalface_alt2.xml')

    cap = cv2.VideoCapture(0)

    while True:
        # capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(10) == ord('q'):
            break
    # when everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    return None


if __name__ == '__main__':
    rec_v()
