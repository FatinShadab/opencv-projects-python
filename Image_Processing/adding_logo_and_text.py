import os
import cv2
import numpy as np
from PIL import (
    Image,
    ImageDraw,
    ImageFont
)

def addWatermark(source_img_path : str, text : str, img_name : str, text_position = 'bottom_right', font_size = 40, imgObj = None, del_source=False):
    if imgObj is None:
        img = Image.open(source_img_path)
    else:
        img = Image.fromarray(np.uint8(imgObj)).convert('RGB')

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('arial.ttf', 30)
    
    text_width, text_height = draw.textsize(text, font)
    img_width, img_height = img.size

    if (text_position == 'bottom_center'):
        x = int(img_width/2) - int(text_width/2)
        y = img_height - text_height - 50
    elif (text_position == 'bottom_right'):
        x = int(img_width) - int(text_width) - 50
        y = img_height - text_height - 50
    elif (text_position == 'bottom_left'):
        x = int(img_width*0) + int(text_width/2)
        y = img_height - text_height - 50
    elif (text_position == 'top_center'):
        x = int(img_width/2) - int(text_width/2)
        y = (img_height*0) + text_height
    elif (text_position == 'top_right'):
        x = int(img_width) - int(text_width) - 50
        y = (img_height*0) + text_height
    elif (text_position == 'top_left'):
        x = int(img_width*0) + int(text_width/2)
        y = (img_height*0) + text_height

    draw.text((x, y), text, font=font)

    img.save(img_name)

    if del_source:
        os.remove(source_img_path)

    return None

def addLogo(source_img_path : str, logo_path : str, save=False, fname='img', ftype='jpg'):
    logo = cv2.imread(logo_path)
    img = cv2.imread(source_img_path)

    rows, cols, channels = logo.shape

    roi = img[0:rows, 0:cols]

    logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

    _, mask = cv2.threshold(logoGray, 220, 255, cv2.THRESH_BINARY)

    inverseMask = cv2.bitwise_not(mask)

    background = cv2.bitwise_and(roi, roi, mask=mask)
    frontImage = cv2.bitwise_and(logo, logo, mask=inverseMask)

    dst = cv2.add(background, frontImage)

    img[0:rows, 0:cols] = dst

    #cv2.imshow('img', img)

    cv2.waitKey(0)

    if save:
        oftype = source_img_path.split('.')[-1]
        
        try:
            f_path = f'{fname}.{oftype}'
            cv2.imwrite(f_path, img)
        except:
            f_path = f'{fname}.{ftype}'
            cv2.imwrite(f_path, img)

        return f_path

    return img


if __name__ == "__main__":
    
    validPositions = [
        'bottom_center',
        'bottom_right',
        'bottom_left',
        'top_center',
        'top_right',
        'top_left',
    ]

    img_pth = "" #image path
    logo_pth = "" # logo path
    text = "" # text
    img_name = "" # output file name


    imgObj = addLogo(img_pth, logo_pth, save=True)

    if type(imgObj) is not str:
        addWatermark(img_pth, text, img_name, font_size=40, imgObj=imgObj)
    else:
        addWatermark(imgObj, text, img_name, font_size=40, del_source=True)