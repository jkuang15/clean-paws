import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib


def initializePinsAndMotor(): # returns tuple with pin numbers and motor
    direction_pin_motor = 40 # REPLACE W REAL PIN
    step_pin_motor = 38 # REPLACE W REAL PIN
    enable_pin_motor = 17 # REAPLCE W REAL PIN (LOW to enable) 
    mode_pins = (-1,-1,-1)
    mymotortest = RpiMotorLib.A4988Nema(direction_pin_motor, step_pin_motor, mode_pins, "DRV8825")
    GPIO.setup(enable_pin_motor,GPIO.OUT)
    return direction_pin_motor, step_pin_motor, mymotortest, enable_pin_motor

def moveMotor(enable_pin_motor, direction_pin_motor, step_pin_motor, mymotortest, step_count, clockwise):
    GPIO.output(enable_pin_motor, GPIO.LOW)
    mymotortest.motor_go(clockwise, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     step_count, # number of steps
                     .0005, # step delay [sec]
                     True, # True = print verbose output 
                     .05) # initial delay [sec]
    mymotortest.motor_stop()
    # mymotortest.motor_stop()

def cleanUpMotor():
    GPIO.cleanup() 

def main():
    direction_pin_motor, step_pin_motor, mymotortest, enable_pin_motor = initializePinsAndMotor()
    moveMotor(enable_pin_motor, direction_pin_motor, step_pin_motor, mymotortest, step_count = 2000, clockwise = False)
    print("here")
    cleanUpMotor()


if __name__ == "__main__":
    main()