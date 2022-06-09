import pyautogui as p

p.leftClick(x=1233, y=3)
p.write('outlook')
p.press('enter')

p.sleep(0.5)

i = 22
numberAttachment = 32
while i <= numberAttachment:
    p.hotkey('command', 'e')
    p.sleep(0.5)
    p.write('{}.pdf'.format(i))
    p.sleep(0.5)
    p.press('enter')
    p.sleep(0.5)
    p.press('up')
    i += 1
