import time
import RPi.GPIO as GPIO

CW = 1
CCW = 0
Dir = 18
Stp = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Dir, GPIO.OUT)
GPIO.setup(Stp, GPIO.OUT)

GPIO.output(Dir, CW)

for i in range(1000):
    GPIO.output(Stp, GPIO.HIGH)
    time.sleep(.01)
    print('here')
    #GPIO.output(Stp, GPIO.LOW)
    time.sleep(.01)

GPIO.cleanup()