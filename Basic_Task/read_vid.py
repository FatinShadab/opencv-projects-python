"""
Basic II : How to read rec videos ?

i) Use 'VideoCapture' func with vid loc address and save in a variable

ii) vidoes are nothing but images so repeat the read_image process 
with while loop

iii) in order to get imgs from video use VideoCapture object's .read() func
which will return a bool value and a image obj

iv) use,
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
to break out of the while loop with 'q' key command
"""


import cv2

def read_video(vid_path):

    cap = cv2.VideoCapture(vid_path)

    while True:
        success, img = cap.read()
        if success:
            cv2.imshow("video", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("pressed q to exit !")
                break
        else:
            print("Ended !")
            break

    return 0

if __name__ == "__main__":

    vid_path = "F:/git/opencv-projects-python/resources/Rotating_earth.gif"
    read_video(vid_path)