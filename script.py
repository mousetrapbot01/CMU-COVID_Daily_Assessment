import webbrowser
import pyautogui
import time

url = 'https://daily-student.cmu.edu/'      
    
#--------------------------------------------------------------------------
# change variables below to those that
# correctly represent what your current condition is

close_contact = False  # True - Have had contact, False - No close contact
any_symptoms  = False  # True - I have symptoms,  False - I don't
temp_higher   = 0      # 1 - Yes,    0 - No,    -1 - I didn't check

#--------------------------------------------------------------------------
webbrowser.open(url)

# wait to give chrome enough time to open
time.sleep(0.1)

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
