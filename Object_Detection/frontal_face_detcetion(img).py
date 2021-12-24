"""
face detection using vilola & jones method 

run the detect_front_face function to see example
*** change the paths of resources according to your file location.
"""

import cv2

def detect_front_face(cascade_path, img_path):
    faceCascade = cv2.CascadeClassifier(cascade_path)
    img = cv2.imread(img_path)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Reasult', img)
    cv2.waitKey(0)

    return 0

if __name__ == "__main__":
    cascade_path = "F:/git/opencv-projects-python/resources/haarcascade_frontalface_alt2.xml"
    img_path = "F:/git/opencv-projects-python/resources/many_ff.jpg"
    detect_front_face(cascade_path, img_path)