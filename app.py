#!/usr/bin/python3
import pyautogui, sys, time
import random
from datetime import datetime
datetime.now()
"""
When fail-safe mode is True, moving the mouse to the upper-left will raise
a pyautogui.FailSafeException that can abort your program.
"""

NUM_TRACKS = 10

# if you set this to true, the program won't wait for your input...
JUST_GO_MODE = False

import logging
import threading
import time
import keyboard

def exit_safe_key_watcher():
    return
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('Esc'):  # if key 'q' is pressed 
            sys.exit()
    except:
        return

# Docs: https://pyautogui.readthedocs.io/en/latest/mouse.html
def double_click_wait(wait=0.2):
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(wait)

def wait_for_human_observer_to_press_enter():
    """
    in just go mode, we don't wait at all.... be careful
    """
    if JUST_GO_MODE:
        return
    print("Waiting for you to press enter...")
    keyboard.wait("Enter")
    print("Gotcha. Proceeding...")

def click_wait(wait=0.1):
    pyautogui.click()
    time.sleep(wait)

def type_a_string(string_to_type):
    pyautogui.write(string_to_type)

def move(x, y):
    pyautogui.moveTo( x ,  y, duration = 0.1)

def open_logic_shortcut():
    """
    Doesn't really work... the app doesn't gain focus
    """
    # Open logic shortcut
    move(688, 112)
    double_click_wait(0.1)
    # Click on "File". this fails
    move( 161,   16)
    click_wait()

def cycle_omnisphere_instrument():
    # Omnisphere random instrument
    # normal position
    # move( 168,  820)

    # default on-open position
    move( 173,  838)

    # This action requires 2 clicks for some reason.
    # and the sleep function messes it up?
    pyautogui.click()
    pyautogui.click()

def minimize_omnisphere_top_pane():
    # move(1398, 61)
    move(1401, 60)
    click_wait()

def pick_random_omnisphere_preset():
    sound_num = random.choice(range(1, 10))
    for n in range(sound_num):
        cycle_omnisphere_instrument()

def open_instrument_window():
     move( 430,  472)
     click_wait()

def pick_track(track_num):
    track_nums = [
        (756,  186),
        (756,  229),
        (760,  284),
        (758,  336),   
        (759,  384),
        (761,  437),
        (761,  480),
        (760,  532),
        (759,  584),
        (763,  634)
    ]
    z = track_nums[track_num]
    move(z[0], z[1])
    click_wait()

def scroll_to_top_of_instrument_pane_in_omnisphere():
    # this functino doesnt wprk and it's slow
    move(217,  614)
    # pyautogui.click()
    # time.sleep(0.1)
    move( 319,  529)
    for n in range(50):
        pyautogui.click()
        # pyautogui.scroll(7)
    # pyautogui.scroll(-50000)

def close_omnisphere():
    move(33, 62)
    click_wait()

def create_random_soundset():
    for i in range(NUM_TRACKS):
        pick_track(i)
        open_instrument_window()
        time.sleep(2)
        minimize_omnisphere_top_pane()
        # scroll_to_top_of_instrument_pane_in_omnisphere()
        pick_random_omnisphere_preset()
        close_omnisphere()
        wait_for_human_observer_to_press_enter()

        # Giving you a chance to do something
        # time.sleep(1)

def current_timestamp_as_string():
    return str(datetime.now()).replace(':', '-').replace(' ', '-').split('.')[0]

def export_to_mp3(filename):
    move( 159,   15) 
    click_wait(0)
    move(224, 460)
    time.sleep(0.2)

    move(499, 457)
    move(522, 528)
    click_wait()
    move(410, 233)
    click_wait()
    move(1029,  546)
    click_wait()
    pyautogui.write(filename)
    move(289, 221)
    click_wait()
    move(480, 167)
    click_wait()

    # This is the moment before a file is saved...
    # Be careful...
    wait_for_human_observer_to_press_enter()
    wait_for_human_observer_to_press_enter()
    pyautogui.press('enter')
    # move(449, 204)

def save():
    pyautogui.hotkey("ctrl", "s")

def save_as(logic_project_filename):
    move( 162,   15)
    click_wait()
    move(196, 184)
    click_wait()
    type_a_string(logic_project_filename)
    move(1180,  821)
    click_wait()
    wait_for_human_observer_to_press_enter()

# pyautogui.moveTo( 161 ,   15, duration = 0.2) 
def set_project_tempo(bpm):
    move(666, 65)
    click_wait(0.4)
    double_click_wait(wait=0.2)
    pyautogui.doubleClick()
    # click_wait()
    #pyautogui.hotkey("ctrl", "a")
    type_a_string(str(bpm))
    pyautogui.press('enter')

def make_soundscapes(how_many=5, bpm=80):
    set_project_tempo(bpm)
    for i in range(how_many):
        save_as("soundscape-v" + str(i))
        create_random_soundset()
        save()
        export_to_mp3("soundscape-v" + str(i) + "--" - current_timestamp_as_string())
        return

make_soundscapes(how_many=3, bpm=80)


# pyautogui.moveTo(100, 100, duration = 0.2)




# pyautogui.click()

# import pyautogui 
# pyautogui.moveTo(0, 50, duration = 1) 


# import pyautogui 
# pyautogui.click(100, 100) 

# import time 

# # a module which has functions related to time. 
# # It can be installed using cmd command: 
# # pip install time, in the same way as pyautogui. 
# import pyautogui 
# time.sleep(10) 

# # makes program execution pause for 10 sec 
# pyautogui.moveTo(1000, 1000, duration = 1) 

# # moves mouse to 1000, 1000. 
# pyautogui.dragRel(100, 0, duration = 1) 

# # drags mouse 100, 0 relative to its previous position, 
# # thus dragging it to 1100, 1000 
# pyautogui.dragRel(0, 100, duration = 1) 
# pyautogui.dragRel(-100, 0, duration = 1) 
# pyautogui.dragRel(0, -100, duration = 1) 


# import pyautogui 
# pyautogui.hotkey("ctrlleft", "a")