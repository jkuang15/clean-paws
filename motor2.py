import RPi.GPIO as GPIO
import time

# GPIO pin numbers
direction_pin = 18
step_pin = 16
enable_pin = 25

# Number of steps per revolution for your specific stepper motor
steps_per_revolution = 1000

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([direction_pin, step_pin, enable_pin], GPIO.OUT)

# Enable the motor (LOW means enabled)
GPIO.output(enable_pin, GPIO.LOW)

# Spin the motor 360 degrees in one direction
GPIO.output(direction_pin, GPIO.HIGH)  # Set direction (HIGH for clockwise, LOW for counterclockwise)
for _ in range(steps_per_revolution):
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.002)  # Adjust this delay based on your motor and driver
    GPIO.output(step_pin, GPIO.LOW)
    time.sleep(0.002)  # Adjust this delay based on your motor and driver

# Pause for a moment
time.sleep(1)

# Spin the motor 360 degrees in the opposite direction
GPIO.output(direction_pin, GPIO.LOW)
for _ in range(steps_per_revolution):
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.002)  # Adjust this delay based on your motor and driver
    GPIO.output(step_pin, GPIO.LOW)
    time.sleep(0.002)  # Adjust this delay based on your motor and driver

# Disable the motor
GPIO.output(enable_pin, GPIO.HIGH)

# Cleanup GPIO when the program exits
GPIO.cleanup()