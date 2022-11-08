import pyautogui as p

# Go to search bar
p.leftClick(x=1220, y=12)
p.write('finder')
p.press('enter')

p.sleep(0.5)