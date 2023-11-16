import RPi.GPIO as GPIO

def turnOn():
    # Set the GPIO pin that is connected to the heatsink to output
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)

    # Turn on the heatsink
    GPIO.output(17, GPIO.HIGH)

if __name__ == "__main__":
    turnOn()