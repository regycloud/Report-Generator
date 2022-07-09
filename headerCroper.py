# Some scrapped graphs from PRTG network monitoring are included some details on the header.
# Crop the selected area to exclude the header by using this headerCropper.

from PIL import Image

def cropImage(cid, startNumber, endNumber):
    nameFile = startNumber
    while nameFile <= endNumber:
        if (cid == 0):
            newNameFile = '{} - SSPL.VAL.13.02.png'.format(nameFile)
        if (cid == 1):
            newNameFile = '{} - SSPL.VAL.13.03.png'.format(nameFile)
        if (cid == 2):
            newNameFile = '{} - SSPL.MIX.011_.png'.format(nameFile)
        if (cid == 3):
            newNameFile = '{} - SSPL.VAL.73.02.png'.format(nameFile)
        if (cid == 4):
            newNameFile = '{} - SSPL.VAL.73.01.png'.format(nameFile)
        if (cid == 5):
            newNameFile = '{} - BKE.VAL.73.01.png'.format(nameFile)
        if (cid == 6):
            newNameFile = '{} - GRNA.VAL.73.01.png'.format(nameFile)

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
        cropped.save(newNameFile)
        print('crop success')

        nameFile = int(nameFile)
        nameFile += 1

# print(findValue('./imgs/graph/3 - SSPL.VAL.13.02.png'))
print(cropImage(1,1,32))
print(cropImage(0,1,32))