#!/usr/bin/python3

"""
When fail-safe mode is True, moving the mouse to the upper-left will raise
a pyautogui.FailSafeException that can abort your program.

Docs: https://pyautogui.readthedocs.io/en/latest/mouse.html

For easy development, run python3 measurement.py in one terminal window
while working on this file. Press enter with the measurement/py window focused to
record that mouse x-y position measurement.
"""
import pyautogui, sys, time
import random
from datetime import datetime
import logging
import threading
import time
import keyboard

# if you set this to true, the program won't wait for your input...
JUST_GO_MODE = True

pyautogui.FAILSAFE = True

def q():
    sys.exit()

def log(x):
    print(x)

def press_enter():
    pyautogui.press('enter')

def exit_safe_key_watcher():
    return
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('Esc'):  # if key 'q' is pressed 
            sys.exit()
    except:
        return

def double_click_wait(wait=0.2):
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(wait)

def wait_for_human_observer_to_press_enter(message):
    """
    in just go mode, we don't wait at all.... be careful
    """
    if JUST_GO_MODE:
        return
    print(message)
    print("Press enter if you want to continue...")
    
    keyboard.wait("Enter")
    print("Gotcha. Proceeding...")

def take_a_screenshot(screenshot_filename='my_screenshot.png'):
    return pyautogui.screenshot(screenshot_filename)

def click_wait(wait=0.1):
    pyautogui.click()
    time.sleep(wait)

def type_a_string(string_to_type):
    pyautogui.write(string_to_type)

def move(x, y=None):
    if y is None:
        pyautogui.moveTo( x[0] ,  x[1], duration = 0.1)
    else:
        pyautogui.moveTo( x ,  y, duration = 0.1)
    
def moveRel(x, y):
    pyautogui.moveRel(x, y, duration=0.1)

def open_logic_shortcut():
    """
    Doesn't really work... the app doesn't gain focus
    """
    # Open logic shortcut
    move(688, 112)
    double_click_wait(0.1)
    # # Click on "File". this fails
    # move( 161,   16)
    # click_wait()
    pyautogui.hotkey("ctrl", "n")

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
    # move(1401, 60)
    move(1379,   41)
    click_wait()

def pick_random_omnisphere_preset(track_num):
    # sound_num = random.choice(range(1, 10))
    good_omnisphere_sounds = [
        { 'name': 'psychopathic whistle', 'roles': ['lead'] },
        { 'name': 'cresting waves', 'roles': ['pad'] },
        { 'name': 'early warmies', 'roles': ['pad'] },
        { 'name': 'JX03', 'roles': ['plink'] },
        { 'name': 'analog chimes', 'roles': ['lead'], 'recommended_range': 'mid'},
        { 'name': 'emptiness', 'roles': ['lead', 'flute'], 'recommended_range': 'mid'},
        { 'name': 'fast chiff heirborne flute', 'roles': ['lead', 'flute']},
    ]
    sound_name = random.choice(good_omnisphere_sounds)['name']
    log('Using sound {} for track {}'.format(sound_name, track_num))
    move(  74,  153) 
    click_wait(0.1)
    click_wait(0.1)
    type_a_string(sound_name)
    press_enter()
    move( 116,  535)
    click_wait(0.1)
    click_wait(0.1)
    # Wait for the patch to load
    time.sleep(0.3)
    

def open_instrument_window():
     move( 430,  472)
     click_wait(1)

def pick_track(track_num):
    track_nums = [
        ( 785,  194),
        ( 801,  242),   
        ( 814,  288),   
        ( 814,  333),   
        ( 819,  384),   
        ( 805,  432),   
        ( 806,  474),   
        ( 809,  515),   
        ( 814,  554),   
        ( 819,  612), 
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
    move(  13,   40)
    click_wait()

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
    pyautogui.press('enter')
    
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

def click_top_of_logic_window():
    move(716, 36)
    click_wait()
    time.sleep(2)
    click_wait()

def drag_instrument_window_to_expected_position():
    import os
    # os.chdir(os.path.dirname(__file__))
    # print(os.getcwd())
    # im2 = pyautogui.screenshot('my_screenshot.png')
    # location = pyautogui.locateOnScreen('imgs/omnisphere-logo.png')
    # print(location)     
    # im2 = pyautogui.screenshot('my_screenshot.png')
    location = pyautogui.locateOnScreen('imgs/instrument-topbar.png')
    print(pyautogui.center(location))
    move(pyautogui.center(location))
    moveRel(0, -89)
    pyautogui.dragTo(117, 26, button='left')

def create_random_soundset(num_tracks):
    for i in range(num_tracks):
        pick_track(i)
        take_a_screenshot()
        time.sleep(0.3)
        open_instrument_window()
        time.sleep(2)
        drag_instrument_window_to_expected_position()
        
        minimize_omnisphere_top_pane()
        # scroll_to_top_of_instrument_pane_in_omnisphere()
        pick_random_omnisphere_preset(i)
        
        wait_for_human_observer_to_press_enter('I picked this preset... do you like it?')
        
        close_omnisphere()
        

def make_beats(how_many_beats=1, bpm=80, num_tracks=10):
    # set_project_tempo(bpm)
    for i in range(how_many_beats):
        # save_as("soundscape-v" + str(i))
        create_random_soundset(num_tracks)
        # save()
        # export_to_mp3("soundscape-v" + str(i) + "--" - current_timestamp_as_string())

def dragTo(x, y):
    pyautogui.mouseDown()
    time.sleep(0.4)
    # pyautogui.dragTo(405, 657, button='left')
    move(x, y)
    pyautogui.mouseUp()

def open_beat_template():
    move( 346,  899)
    time.sleep(0.3)
    move( 333,  836)
    dragTo(405, 657)
    click_wait(0)
    time.sleep(0.4)
    pyautogui.mouseUp()
    time.sleep(0.5)
    click_top_of_logic_window()

open_beat_template()

make_beats(how_many_beats=1, bpm=80, num_tracks=3)

print("All done.")


q()