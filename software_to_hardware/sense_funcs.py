#Raspberry Pi 4.0 code for interfacing with ultrasonic sensor

import RPi.GPIO as GPIO #importing modules required in program
import time #to add delays 

GPIO.setmode(GPIO.BOARD) 


def move(tri, ech):


    GPIO.setup(tri, GPIO.OUT) #trig pin is output
    GPIO.setup(ech, GPIO.IN) #echo pin is input
    GPIO.output(tri, GPIO.LOW) #drives trig pin to OV

    time.sleep(2) #delay 2 secs

    GPIO.output(tri, GPIO.HIGH) #set trig pin high

    time.sleep(0.00001)

    GPIO.output(tri, GPIO.LOW)

    #print(GPIO.input(ech))

    while GPIO.input(ech) == 0:
        send = time.time() 
        #print('send is', send)

    while GPIO.input(ech) == 1:
        receive = time.time()
       # print('receive is', receive)

    duration = receive - send 

    duration = round(34000* duration/2, 2)

    distance = duration#34000* duration 

    print("obj at " + str(distance) + " CM from ultra sensor")

    GPIO.cleanup()

    return str(distance)



