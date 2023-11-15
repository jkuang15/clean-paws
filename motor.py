import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib


def initializePinsAndMotor(): # returns tuple with pin numbers and motor
    direction_pin_motor = 22 # REPLACE W REAL PIN
    step_pin_motor = 23 # REPLACE W REAL PIN
    enable_pin_motor = 24 # REAPLCE W REAL PIN (LOW to enable) 
    mymotortest = RpiMotorLib.A4988Nema(direction_pin_motor, step_pin_motor, (21,21,21), "DRV8825")
    GPIO.setup(enable_pin_motor,GPIO.OUT)
    return direction_pin_motor, step_pin_motor, enable_pin_motor, mymotortest

def moveMotorToPaper(direction_pin_motor, step_pin_motor, enable_pin_motor, mymotortest):
    GPIO.output(enable_pin_motor, GPIO.LOW)
    mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     200, # number of steps
                     .0005, # step delay [sec]
                     False, # True = print verbose output 
                     .05) # initial delay [sec]
    mymotortest.motor_stop()
    mymotortest.motor_stop()

def cleanUpMotor():
    GPIO.cleanup() 

def main():
    motor_tuple = initializePinsAndMotor()
    moveMotorToPaper(motor_tuple)
    cleanUpMotor()
