import pyautogui
# size of desctop
width, height = pyautogui.size()
# print(pyautogui.size())
print(pyautogui.position())

#move cursor
pyautogui.moveTo(400, 320, duration=0.5)
print(pyautogui.position())

#click mouse (right left middle)
pyautogui.click(400, 320, button='left')


#drag upline
# pyautogui.easeInQuad   # start slow, end fast
# pyautogui.easeOutQuad   # start fast, end slow
# pyautogui.easeInOutQuad  # start and end fast, slow in middle
# pyautogui.easeInBounce  # bounce at the end
# pyautogui.easeInElastic  # rubber band at the end
pyautogui.dragTo(740, 320,1,pyautogui.easeInQuad)


# cut line by keyboard and pase by mouse
pyautogui.keyDown('ctrl')
pyautogui.keyDown('x')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('x')
pyautogui.click(400, 320, button='right')
pyautogui.moveTo(450, 350, duration=0.5)
#other whay to click
pyautogui.mouseDown(button='left')
pyautogui.mouseUp()
# pyautogui.click(450, 350, button='left')

#down
#scroll
pyautogui.scroll(-1000)
#up
pyautogui.scroll(100)

# keyboard write
# pyautogui.click(400, 600, button='left')
# pyautogui.write('Hello world!')#, interval=0.25

