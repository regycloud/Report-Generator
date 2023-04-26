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
                                    
                                # newValue = d['text'][i].replace('.','')
                                # newValue = d['text'][i].replace(',','')
                                # newValue = int(newValue)/1000
                                # newValue = str(newValue)

                                percentileValues.append(d['text'][i])

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
            # method 2, store all result in an array
            allResults.append(d['text'][i])
            
    value.append(percentileValues)
    value.append(averageValues)
    value2[1].append(allResults[15])
    value2[1].append(allResults[23])
    value2[0].append(allResults[17])
    value2[0].append(allResults[25])
    print(" ")
    if (allResults[16] == 'Mbit/s'):
        def inKB(n):
            try:
                return int(allResults[n]) * 1000
            except:
                if (re.search(r'\d\.\d', str(allResults[n]))):
                    allResults[n] = str(allResults[n]).replace('.','')
                    return int(allResults[n]) * 10
                if (re.search(r'\d\,\d', str(allResults[n]))):
                    allResults[n] = str(allResults[n]).replace(',','')
                    return int(allResults[n])

        value2[1][0] = inKB(15)
        value2[1][1] = inKB(23)
        value2[0][0] = inKB(17)
        value2[0][1] = inKB(25)




    # [[percentile in, percentile out], [average in, average out]]
    # those return value are in kb
    return value2
# a = findValue('./imgs/table/1 - SSPL.VAL.13.03.png')
# print(findValue('./imgs/table/1 - SSPL.VAL.73.03.png'))
