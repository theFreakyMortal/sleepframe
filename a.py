import pyautogui
import time
from pynput import keyboard

def focus_warframe():
    for window in pyautogui.getWindowsWithTitle("Warframe"):
        window.activate()
        break

focus_warframe()
time.sleep(.2)
pyautogui.screenshot("screenshot.png", region=(1475, 135, 290, 50))
