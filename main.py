# main.py
from roboflow import Roboflow
#import RPi.GPIO as GPIO
#from RpiMotorLib import RpiMotorLib
import time

#TODO: 
# - website /
# - detection for object in tray /
# - conveyor belt motor control
# - dumping motor control
# - ultrasonic sensor + website update



rf = Roboflow(api_key="79w38aK1oCiq60ZrVmG1")
project = rf.workspace().project("recyclables-ilmxu")
model = project.version(1).model




def print_prediction(lst):
    for pic in image_list:
        print(model.predict(pic, confidence=0, overlap=30).json())


if __name__ == "__main__":
    image_list = ["images/plastic-bottle-ground.jpeg", "images/plastic-fork.png", "images/water-bottle.jpeg", 
                "images/red-straw.jpeg", "images/cocacola-can.jpeg", "images/fork-chair.jpeg", "images/fork-ground.jpeg",
                "images/fork-table.jpeg"]
    # no image list (just one image)

    print_prediction(image_list)



# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())