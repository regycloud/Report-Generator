from unicodedata import name
from PIL import Image
from pdf2image import convert_from_path
from findTableBorder import findValue

    # Select page by CID
    # 0 LINK#1
    # 1 LINK#2
    # 2 SSPL.MIX1.011
    # 3 SSPL.VAL.73.02
    # 4 SSPL.VAL.73.01
    # 5 BKE.VAL.73.01
    # 6 GRNA.VAL.73.01

def createTable(cid,stardate, endDate):
    nameFile = stardate
    while int(nameFile) <= endDate:
        nameFile = str(nameFile)
        pages = convert_from_path('{}.pdf'.format(nameFile), 500)

        for i in range(len(pages)):
            break # Go for GRNA only
            # print("This pdf has {} pages".format(i))
            pages[i].save('{}.png'.format(i), 'PNG')
            im = Image.open('{}.png'.format(i))
                #  x = 306
                #  left = x - 16
                #  y = 4954
                #  right = y - 19
            x = findValue(i)[0] - 16
            y = findValue(i)[1] - 19
            a = x + 3415
            b = y + 295
                
                # 306 4954 == 306 - 16
                # 4954 - 19
                #  Table size 
                #  Width: 3415 px
                #  Height: 295 px
            cropped = im.crop((x,y,a,b)) # left, top, right, bottom
            if i == 0:
                cropped.save('{} Link#1.png'.format(nameFile))
            if i == 1:
                cropped.save('{} Link#2.png'.format(nameFile))
            if i == 2:
                cropped.save('{} SSPL.MIX.011.png'.format(nameFile))
            if i == 3:
                cropped.save('{} Link#1.png'.format(nameFile))
            if i == 4:
                cropped.save('{} Link#1.png'.format(nameFile))
            if i == 5:
                cropped.save('{} Link#1.png'.format(nameFile))
            if i == 6:
                cropped.save('{} Link#1.png'.format(nameFile))
        
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
        # Select page by CID
        # 0 LINK#1
        # 1 LINK#2
        # 2 SSPL.MIX1.011
        # 6 GRNA.VAL.73.01
        pages[cid].save(newNameFile, 'PNG')
        im = Image.open(newNameFile.format(nameFile))
            #  x = 306
            #  left = x - 16
            #  y = 4954
            #  right = y - 19
        x = findValue(newNameFile)[0] - 16
        y = findValue(newNameFile)[1] - 19
        a = x + 3415
        b = y + 295
        cropped = im.crop((x,y,a,b))
        cropped.save(newNameFile)

        nameFile = int(nameFile)
        nameFile += 1

createTable(0,8,32)
createTable(1,8,32)
createTable(3,8,32)