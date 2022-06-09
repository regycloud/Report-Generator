import cv2
import re
from numpy import append
import pytesseract
from pytesseract import Output



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
    averageValues = []
    percentileValues = []
    # img = cv2.imread('{} - SSPL.VAL.13.02.png'.format(image))
    img = cv2.imread('imgs/{} - SSPL.VAL.13.02.png'.format(image))

    # convert_grayscale(img)
    # threshold(img)
    pre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 11'


    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    keys = list(d.keys())

    found = 0
    # xStart = 999
    # xEnd = 999
    # yStart = 999
    

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 0:
            # if re.match(total_pattern, d['text'][i]):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            
            # Illustration for x,y in in cv2            
            # 0
            # |------ x
            # |
            # y

            #### x axis boundaries
            # Find the word 'Percentile' to 
            if re.search(r"\bPerc\w+", d['text'][i]):
                # print(d['text'][i], x, y, 'should be percentile') # use this x-start as a row boundary
                found += 1
                xStart = x


            # # Find the word 'Total' with regex Tot...
            if re.search(r"\bTot\w+", d['text'][i]):
                # print(d['text'][i], x, y, 'should be total') # use this x-end as a column boundary
                found += 1
                if found == 2:
                    xEnd = x

            if re.search(r"\bAve\w+", d['text'][i]):
                # print(d['text'][i], x, y, 'should be Average') # use this x-start as a row boundary
                xAverage = x
                foundAverage = 1

            # #### y axis boundaries
            # # Find the word 'Total' with regex Tot...
            if re.search(r"In", d['text'][i]):
                # print(d['text'][i], x, y, 'should be Traffic In') # use this y-end as a row boundary
                yStart = y

            if re.search(r"Out", d['text'][i]):
                # print(d['text'][i], x, y, 'should be Traffic Out') # use this y-end as a row boundary
                yOut = y

            try:

                if (found >= 2):
                    if (x > xStart and x < xEnd):
                        if (y >= yStart -1):
                            if (re.findall("\d", d['text'][i])):
                                # replace comma, convert to kbit to Mbit, and change to string again
                                newValue = d['text'][i].replace(',','')
                                newValue = int(newValue)/1000
                                newValue = str(newValue)

                                percentileValues.append(newValue)

                if (foundAverage == 1):
                    if (x > xAverage and x < xStart):
                        if (y >= yStart -1):
                            if (re.findall("\d", d['text'][i])):
                                # replace comma, convert to kbit to Mbit, and change to string again
                                averageValue = d['text'][i].replace(',','')
                                averageValue = int(averageValue)/1000
                                averageValue = str(averageValue)

                                averageValues.append(averageValue)
            except:
                pass
    value.append(percentileValues)
    value.append(averageValues)
    return value

print(findValue('1'))