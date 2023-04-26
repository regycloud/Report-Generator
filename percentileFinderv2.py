# This file is intended to read the specified data on the table (./imgs/table) and store them in array which will be used in excelDataAndImageAuto.py.

from distutils.command.config import config
import cv2
import re
import pytesseract
from pytesseract import Output


# Options to amplify the recognization text by pytesseract
def convert_grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def blur(img, param):
    img = cv2.medianBlur(img, param)
    return img

def threshold(img):
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img


def findValue(image):
    value = []
    value2 = [[],[]]
    averageValues = []
    percentileValues = []
    allResults = []
    # img = cv2.imread('{} - SSPL.VAL.13.02.png'.format(image))
    img = cv2.imread('{}'.format(image))
    resize = cv2.resize(img, None, fx=6.5, fy=6.5, interpolation=cv2.INTER_CUBIC)
    bw = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)


    # convert_grayscale(img)
    # threshold(img)
    pre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    custom_config = r'--psm 4 --oem 3'


    d = pytesseract.image_to_data(bw, output_type=Output.DICT, config=custom_config)
    keys = list(d.keys())

    found = 0
    # xStart = 999
    # xEnd = 999
    # yStart = 999
    

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 0:
            allResults.append(d['text'][i])


    print(allResults)
    digitIndex = []

    # Find the 
    for i in range(len(allResults)):
        item = allResults[i]
        if item:
            if item[0].isdigit():
                digitIndex.append(i)
    print(digitIndex)

    # Check



    # [[percentile in, percentile out], [average in, average out]]
    # those return value are in kb
    # return value2
# a = findValue('./imgs/table/29 - SSPL.VAL.13.02.png')
a = findValue('./imgs/table/7 - SSPL.VAL.73.02.png')
