import time
import random
import threading
import pyautogui
import pytesseract
from pynput import keyboard
from pynput.keyboard import Controller

keyboard_controller = Controller()
status = False
frame = False
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def flipflop(key):
    global status
    try:
        if key.char == 'j':
            status = not status
    except AttributeError:
        pass

def scan_screenshot():
    global frame
    while True:
        if status:
            screenshot = pyautogui.screenshot(region=(1475, 135, 290, 50))
            text = pytesseract.image_to_string(screenshot)
            if "EXCALIBUR UMBRA" in text:
                frame = True
                print("Umbra detected")
            else:
                frame = False
                print("Umbra not detected")
        time.sleep(0.1)

def walk():
    while True:
        if status == True:
            keyboard_controller.press('w')
            keyboard_controller.press('a')
        if status == False:
            keyboard_controller.release('w')
            keyboard_controller.release('a')
        time.sleep(0.1)

def protect():
    while True:
        if status and not frame:
            keyboard_controller.press(' ')
            time.sleep(random.uniform(0.02, 0.04))
            keyboard_controller.release(' ')
            time.sleep(random.uniform(0.13, 0.16))
            keyboard_controller.press(' ')
            time.sleep(random.uniform(0.02, 0.04))
            keyboard_controller.release(' ')
            time.sleep(random.uniform(4.5, 4.8))
        time.sleep(0.1)

def anti_afk():
    while True:
        if status:
            keyboard_controller.press('5')
            time.sleep(random.uniform(0.02, 0.04))
            keyboard_controller.release('5')
            time.sleep(random.uniform(13, 17))
        time.sleep(0.1)

def changer():
    while True:
        if frame:
            keyboard_controller.press('5')
            time.sleep(random.uniform(0.02, 0.04))
            keyboard_controller.release('5')
            time.sleep(random.uniform(0.13, 0.16))
        time.sleep(0.1)

def main():
    threads = []
    threads.append(threading.Thread(target=anti_afk))
    threads.append(threading.Thread(target=changer))
    threads.append(threading.Thread(target=walk))
    threads.append(threading.Thread(target=protect))
    threads.append(threading.Thread(target=scan_screenshot))

    for thread in threads:
        thread.start()

    with keyboard.Listener(on_press=flipflop) as listener:
        listener.join()

if __name__ == "__main__":
    main()