import RPi.GPIO as GPIO
from time import sleep

DIR = 18   # Direction GPIO Pin
STEP = 16  # Step GPIO Pin
MS1 = 16   # Microstep Resolution GPIO Pin
MS2 = 12   # Microstep Resolution GPIO Pin
ENABLE = 25  # Enable GPIO Pin

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200  # Steps per Revolution (200 steps for DRV8825 in full step mode)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(ENABLE, GPIO.OUT)

# Set microstep resolution (Full step mode in this example)
GPIO.output(MS1, GPIO.LOW)
GPIO.output(MS2, GPIO.LOW)

# Enable the motor (LOW means enabled)
GPIO.output(ENABLE, GPIO.LOW)

def step_motor(direction, steps, delay):
    GPIO.output(DIR, direction)

    for _ in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

# Spin the motor 360 degrees in one direction
step_motor(CW, SPR, 0.002)

# Pause for a moment
sleep(1)

# Spin the motor 360 degrees in the opposite direction
step_motor(CCW, SPR, 0.002)

# Disable the motor
GPIO.output(ENABLE, GPIO.HIGH)

# Cleanup GPIO when the program exits
GPIO.cleanup()