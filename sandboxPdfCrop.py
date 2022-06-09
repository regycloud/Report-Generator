from doctest import OutputChecker
import pygetwindow as pg
import pyautogui as p

from PyPDF2 import PdfFileReader, PdfFileWriter
# print(pg.getAllTitles())

# p.locateOnScreen('anydesk')

with open('1.pdf', 'rb') as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter

    numPages = input1.getNumPages()
    print("This document has {} pages".format(numPages))