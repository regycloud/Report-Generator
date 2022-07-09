# This file is intended to read the specified data on the table (./imgs/table) and store them in array which will be used in excelDataAndImageAuto.py.

import cv2
import re
import pytesseract
from pytesseract import Output



def convert_grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def threshold(img):
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img

def findValue(image):
    value = []
    img = cv2.imread('{}'.format(image))

    # Use this option, if the result from pytesseract is not recognised.

    # convert_grayscale(img)
    # threshold(img)
    # pre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # custom_config = r'--oem 3 --psm 11'

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    keys = list(d.keys())    


    # Define the text on the image through boxes for each word.
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 0:
            # if re.match(total_pattern, d['text'][i]):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            # Reference for defining x and y on the picture.
            #     print(d['text'][4])
            # |------ x
            # |
            # y

            # Find the word started by "Cha.." on the words. 
            if re.search(r"\bCha\w+", d['text'][i]):
                value = [x, y]

    return value


