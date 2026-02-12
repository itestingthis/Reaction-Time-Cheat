# ==== reactionTimeCheat/main.py ==== #

# this script automates clicking on specific colors on the screen.

import pyautogui
import time

while True:
    r, g, b = pyautogui.screenshot().getpixel((200, 500))
    print(f"Renk: ({r}, {g}, {b})")


    if (r, g, b) == (75, 219, 106):  # green color
        pyautogui.click(200, 500)  # click
        print("green color detected, clicked")
        time.sleep(1)

    elif (r, g, b) == (43, 135, 209):  # blue color
        pyautogui.click(200, 500)  # click
        print("blue color detected, clicked")

# 43, 135, 209 blue
# 75, 219, 106 green

# this program created for this website --> https://humanbenchmark.com/tests/reactiontime
