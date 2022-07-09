from datetime import date
import pyautogui as p

dateStart = 1
# Go to search bar
p.leftClick(x=1220, y=12)
p.write('Anydesk')
p.press('enter')

p.sleep(0.5)

# Go to Adress bar 
p.leftClick(x=510, y=110)
p.press('left')
p.press('right', presses=65)
p.press('delete', presses=2)
if dateStart < 10:
    dateStart = str(dateStart)
    inputDate = '0{}'.format(dateStart)
else:
    inputDate = str(dateStart)
p.write(inputDate)

p.sleep(0.5)

p.press('right', presses=24)
p.press('delete', presses=2)
p.write(inputDate)
p.press('enter')

p.sleep(0.5)

# Go to search bar
p.leftClick(x=1220, y=12)
p.write('Preview')
p.press('enter')

p.sleep(0.5)

# Select Screenshot menu on Preview
p.leftClick(x=110, y=1)
p.leftClick(x=404, y=381)

p.sleep(1)


# Do the screenshot from bottom
p.moveTo(x=57, y=660)
p.dragTo(x=860, y=427, duration=0.5)

p.sleep(0.5)


# Save the ScreenShot:
p.moveTo(x=110, y=1)
p.leftClick(x=167, y=165)

p.sleep(1)

# Rename the file
p.write(inputDate)
p.press('enter')

p.sleep(0.5)

# Close the preview
p.leftClick(x=77, y=8)
p.leftClick(x=105, y=210)