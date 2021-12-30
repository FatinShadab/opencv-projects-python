import numpy as np
import cv2

image = cv2.imread('scan.png')

img = cv2.resize(image, (960, 540))
imCanny = cv2.Canny(img, 150, 200)

contours, hierarchy = cv2.findContours(imCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
imgsh = img.copy()

final_con = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 7900 and area > 1300:
        final_con.append(cnt)
        peri = cv2.arcLength(cnt, True) 
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) 
        cv2.drawContours(imgsh, [approx], -1, (0, 255, 0), 2)


idx = 0
for c in final_con: 
    x,y,w,h = cv2.boundingRect(c) 
    if w<100: 
        idx+=1
        new_img=img[y:y+h,x:x+w] 
        cv2.imwrite(str(idx) + '.png', new_img) 


cv2.imshow('finalImg2', imCanny)
cv2.imshow('finalImg', imgsh)
cv2.imshow("im",img) 
cv2.waitKey(0)

