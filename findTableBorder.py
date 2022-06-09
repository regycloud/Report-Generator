import cv2
import re
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
    img = cv2.imread('{}'.format(image))

    # convert_grayscale(img)
    # threshold(img)
    pre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 11'


    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    keys = list(d.keys())

    found = 0
    xStart = 0
    xEnd = 0
    yStart = 9999
    

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 0:
            # if re.match(total_pattern, d['text'][i]):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            #     print(d['text'][4])
            

            # |------ x
            # |
            # y

            #### x axis boundaries
            # Find the word 'Percentile' to 
            if re.search(r"\bCha\w+", d['text'][i]):
                # print(d['text'][i], x, y, 'should be percentile') # use this x-start as a row boundary
                value = [x, y]

            # try: 
            #     a = re.search(r"\bggg\w+", d['text'][i])
            #     # print(a.group(), x, y, d['conf'][i])
            #     print(type(a.group()))
            # except:
            #     print('no words found')

    return value


