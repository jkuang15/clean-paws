from time import sleep
import RPi.GPIO as GPIO

DIR = 18   # Direction GPIO Pin
STEP = 16  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(DIR, GPIO.OUT) 
GPIO.setup(STEP, GPIO.OUT) 
GPIO.output(DIR, CW) 
#p=GPIO.PWM(en,1000)
#p.start(25)

step_count = SPR
delay = .0208

def run_motor():
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        print("hello")
        #GPIO.output(STEP, GPIO.LOW)
        #sleep(delay)

    GPIO.cleanup()

if __name__ == '__main__': 
    run_motor()

# sleep(.5)
# GPIO.output(DIR, CCW)
# for x in range(step_count):
#     GPIO.output(STEP, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP, GPIO.LOW)
#     sleep(delay)


