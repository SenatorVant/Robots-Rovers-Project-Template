import keyboard
from motors import *

print("WASD to drive | Q to quit")

while True:

    if keyboard.is_pressed('w'):
        move_forward()

    elif keyboard.is_pressed('s'):
        move_backward()

    elif keyboard.is_pressed('a'):
        turn_left()

    elif keyboard.is_pressed('d'):
        turn_right()

    else:
        stop()

    if keyboard.is_pressed('q'):
        stop()
        break
