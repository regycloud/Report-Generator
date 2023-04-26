# Some scrapped graphs from PRTG network monitoring are included some details on the header.
# Crop the selected area to exclude the header by using this headerCropper.

from PIL import Image
from daysNumber import daysNumber

def cropImage(cid, startNumber, endNumber, daysNumber):
    nameFile = startNumber
    while nameFile <= endNumber:
        if daysNumber == 30:
            if nameFile == 31:
                nameFile = 32
        if (cid == 0):
            newNameFile = '{} - SSPL.VAL.13.02.png'.format(nameFile)
        if (cid == 1):
            newNameFile = '{} - SSPL.VAL.13.03.png'.format(nameFile)
        if (cid == 2):
            newNameFile = '{} - SSPL.MIX1.011.png'.format(nameFile)
        if (cid == 3):
            newNameFile = '{} - SSPL.VAL.73.02.png'.format(nameFile)
        if (cid == 4):
            newNameFile = '{} - SSPL.VAL.73.01.png'.format(nameFile)
        if (cid == 5):
            newNameFile = '{} - BKE.VAL.73.01.png'.format(nameFile)
        if (cid == 6):
            newNameFile = '{} - GRNA.VAL.73.01.png'.format(nameFile)
        def crop():
            im = Image.open('./imgs/graph/{}'.format(newNameFile))
                #  x = 306
                #  left = x - 16
                #  y = 4954
                #  right = y - 19
            width, height = im.size

            # x = findValue('./imgs/graph/{}'.format(newNameFile))[1]
            # print(width, height, x)
            # cropped = im.crop((0, width-x - 20, width, height))
            cropped = im.crop((0, 33, width, height))
            cropped.save("./imgs/graph/" + newNameFile)
            print('crop success')
            nameFile += 1


        try:
            crop()

        except:
            nameFile = int(nameFile)
            nameFile += 1


# print(findValue('./imgs/graph/3 - SSPL.VAL.13.02.png'))
# crop Image (cid, start, end, func(daysNumber))
# daysNumber = daysNumber(2021, 11)
# print(cropImage(0,1,32,daysNumber))
# print(cropImage(1,1,32,daysNumber))
# print(cropImage(4,1,32,daysNumber))
# i = 0
# while i <= 6:
#     cropImage(i, 1, 32, daysNumber(2021, 12))
#     i += 1
# cropImage(0, 32, 32, daysNumber=(2023, 1))
cropImage(0, 1, 32, 32)
cropImage(2, 1, 32, 32)
# print('error')
# cropImage(6, 1, 32, daysNumber=(2022, 12))

# if (cid == 0):
# newNameFile = '{} - SSPL.VAL.13.02.png'.format(nameFile)
# if (cid == 1):
# newNameFile = '{} - SSPL.VAL.13.03.png'.format(nameFile)
# if (cid == 2):
# newNameFile = '{} - SSPL.MIX.011_.png'.format(nameFile)
# if (cid == 3):
# newNameFile = '{} - SSPL.VAL.73.02.png'.format(nameFile)
# if (cid == 4):
# newNameFile = '{} - SSPL.VAL.73.01.png'.format(nameFile)
# if (cid == 5):
# newNameFile = '{} - BKE.VAL.73.01.png'.format(nameFile)
# if (cid == 6):
# newNameFile = '{} - GRNA.VAL.73.01.png'.format(nameFile)