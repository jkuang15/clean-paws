# main.py
from roboflow import Roboflow
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time



rf = Roboflow(api_key="79w38aK1oCiq60ZrVmG1")
project = rf.workspace().project("recyclables-ilmxu")
model = project.version(1).model

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



def print_prediction(lst):
    for pic in image_list:
        print(model.predict(pic, confidence=0, overlap=30).json())

def cleanUpMotor():
    GPIO.cleanup() 

if __name__ == "__main__":
    image_list = ["images/plastic-bottle-ground.jpeg", "images/plastic-fork.png", "images/water-bottle.jpeg", 
                "images/red-straw.jpeg", "images/cocacola-can.jpeg", "images/fork-chair.jpeg", "images/fork-ground.jpeg",
                "images/fork-table.jpeg"]
    # no image list (just one image)

    print_prediction(image_list)


    # Motor control 

    motor_tuple = initializePinsAndMotor()
    moveMotorToPaper(motor_tuple)
    cleanUpMotor()




# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())