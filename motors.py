import RPi.GPIO as GPIO
from config import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in (LEFT_IN1, LEFT_IN2, RIGHT_IN1, RIGHT_IN2):
    GPIO.setup(pin, GPIO.OUT)

def move_forward():
    GPIO.output(LEFT_IN1, GPIO.HIGH)
    GPIO.output(LEFT_IN2, GPIO.LOW)
    GPIO.output(RIGHT_IN1, GPIO.HIGH)
    GPIO.output(RIGHT_IN2, GPIO.LOW)

def move_backward():
    GPIO.output(LEFT_IN1, GPIO.LOW)
    GPIO.output(LEFT_IN2, GPIO.HIGH)
    GPIO.output(RIGHT_IN1, GPIO.LOW)
    GPIO.output(RIGHT_IN2, GPIO.HIGH)

def turn_left():
    GPIO.output(LEFT_IN1, GPIO.LOW)
    GPIO.output(LEFT_IN2, GPIO.HIGH)
    GPIO.output(RIGHT_IN1, GPIO.HIGH)
    GPIO.output(RIGHT_IN2, GPIO.LOW)

def turn_right():
    GPIO.output(LEFT_IN1, GPIO.HIGH)
    GPIO.output(LEFT_IN2, GPIO.LOW)
    GPIO.output(RIGHT_IN1, GPIO.LOW)
    GPIO.output(RIGHT_IN2, GPIO.HIGH)

def stop():
    for pin in (LEFT_IN1, LEFT_IN2, RIGHT_IN1, RIGHT_IN2):
        GPIO.output(pin, GPIO.LOW)
