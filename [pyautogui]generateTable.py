import pyautogui as p


startDate = 8

while startDate <= 30:
    endDate = startDate + 1
    # Go to search bar  2022-05-1       2022-
    p.leftClick(x=1233, y=3)
    p.write('Anydesk')
    p.press('enter')
    p.leftClick(x=524, y=266)
    p.press('tab')
    startDate = str(startDate)
    inputStarDate = '2021-07-{}'.format(startDate)
    p.write(inputStarDate)

    p.sleep(1)


    p.press('tab')
    endDate = str(endDate)
    inputEndDate = '2021-07-{}'.format(endDate)
    p.write(inputEndDate)
    p.press('esc')

    p.sleep(1)

    # select file format
    p.leftClick(x=217, y=559)


    # Target Email Address
    p.press('tab')
    p.press('left')
    p.press('delete', presses=12)
    p.write('regy')
    p.press('tab')

    p.sleep(1)

    p.press('enter')

    p.sleep(5)
    # click back on browser
    p.leftClick(x=55, y=107)
    p.sleep(2)
    startDate = int(startDate)
    startDate = startDate + 1
    endDate = int(endDate)
