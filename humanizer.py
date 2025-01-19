import time
from pynput import keyboard
from pynput.keyboard import Controller

keyboard_controller = Controller()
crntTime = None

def on_press(key):
    global crntTime
    if crntTime:
        elapsed_time = time.time() - crntTime
        print(f"Elapsed time: {elapsed_time} seconds")
    crntTime = time.time()

with keyboard.Listener(on_press=on_press, on_release=on_press) as listener: 
    listener.join()                                                     