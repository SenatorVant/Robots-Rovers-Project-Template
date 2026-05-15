import time
from motors import *
from ultrasonic import get_distance
from config import *

print("Autonomous mode started")

try:
    while True:
        distance = get_distance()

        print(f"Distance: {distance} cm")

        if distance > OBSTACLE_DISTANCE_CM:
            move_forward()
        else:
            stop()
            move_backward()
            time.sleep(0.5)
            turn_right()
            time.sleep(0.5)
            stop()

        time.sleep(0.1)

except KeyboardInterrupt:
    stop()
