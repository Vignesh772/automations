import pyautogui
import time
time.sleep(5)

j=1
directions=1
i=0

for i in range(150):
    pyautogui.write("#"*j)
    pyautogui.press("enter")
    if directions:
        j+=1
    else:
        j-=1
    if j==15:
        directions=0
    if j==0:
        directions=1