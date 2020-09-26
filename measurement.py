#!/usr/bin/python3
import pyautogui, sys, time


try:
    while True:
        x, y = pyautogui.position()
        # positionStr = ('  pyautogui.moveTo(' + str(x).rjust(4) + ' , ' + str(y).rjust(4) + ', duration = 0.2)   ')
        positionStr = ('  move('+ str(x).rjust(4) + ', ' + str(y).rjust(4) + ')   ')
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')