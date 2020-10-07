# install webbrowser and pyautogui from pip
# the way to do so is
# pip install _

import webbrowser
import pyautogui
import time

# change specify chrome application location
# Below are default values for common OS types
# I have only tested in windows - please help test in other environments

windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
mac     = 'open -a /Applications/Google\ Chrome.app %s'
linux   = '/usr/bin/google-chrome %s'

# make sure you are signed into your andrew id before running this script
# or else it will prompt the login interface instead of this url
url = 'https://daily-student.cmu.edu/'      
    
#--------------------------------------------------------------------------
# change variables below to those that
# correctly represent what your current condition is


close_contact = False  # True - Have had contact, False - No close contact
any_symptoms  = False  # True - I have symptoms,  False - I don't
temp_higher   = 0      # 1 - Yes,    0 - No,    -1 - I didn't check
OS_type                                  = windows

#--------------------------------------------------------------------------
        
chrome_path = OS_type
webbrowser.get(chrome_path).open(url)

# wait to give chrome enough time to open
time.sleep(0.5)

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

if not close_contact:
    pyautogui.hotkey('right')
pyautogui.hotkey('space')
pyautogui.hotkey('tab')

if not any_symptoms:
    pyautogui.hotkey('right')
pyautogui.hotkey('space')
pyautogui.hotkey('tab')

if temp_higher == 0:
    pyautogui.hotkey('right')
if temp_higher == -1:
    pyautogui.hotkey('right')
    pyautogui.hotkey('right')

pyautogui.hotkey('space')
pyautogui.hotkey('tab')

# WARNING: uncommenting this line will press submit!
#pyautogui.hotkey('space')
