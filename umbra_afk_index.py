import time
import random
import threading
from pynput import keyboard
from pynput.keyboard import Controller

keyboard_controller = Controller()
status = False

def flipflop(key):
    global status
    try:
        if key.char == 'j':
            status = not status
    except AttributeError:
        pass

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
        if status:
            keyboard_controller.press(' ')
            time.sleep(random.uniform(0.02, 0.04))
            keyboard_controller.release(' ')
            time.sleep(random.uniform(0.13, 0.16))
            keyboard_controller.press(' ')
            time.sleep(random.uniform(0.02, 0.04))
            keyboard_controller.release(' ')
            time.sleep(random.uniform(4.6, 4.9))
        time.sleep(0.1)

def anti_afk():
    while True:
        if status:
            keyboard_controller.press('5')
            time.sleep(random.uniform(0.02, 0.04))
            keyboard_controller.release('5')
            time.sleep(random.uniform(0.9, 1.1))
            keyboard_controller.press('5')
            time.sleep(random.uniform(0.02, 0.04))
            keyboard_controller.release('5')
            time.sleep(random.uniform(25, 35))
        time.sleep(0.1)

def printer():
    while True:
        print("Status: ", status)
        time.sleep(1)
    
def main():
    threads = []
    threads.append(threading.Thread(target=printer))
    threads.append(threading.Thread(target=walk))
    threads.append(threading.Thread(target=protect))
    threads.append(threading.Thread(target=anti_afk))

    for thread in threads:
        thread.start()

    with keyboard.Listener(on_press=flipflop) as listener:
        listener.join()

if __name__ == "__main__":
    main()