# clean-paws
# DB Engineering Project: Clean Paws - Automated Recycling Bin

# TABLE OF CONTENTS

### [Introduction](#introduction)

### [Installation](#installation)

### [Usage](#usage)

### [Acknowledgements](#acknowledgements)

## Introduction

Have the latest version of Python installed on your computer.
https://www.python.org/downloads/ 

Clean Paws is a smart recycling bin that is designed to enhance the efficiency of recyclable sorting. It utilizes technology to address environmental challenges, offering an intelligent and convenient solution for effective recycling. This system integrates a metal detector, a camera, and machine learning algorithms to identify and categorize items into 3 distinct bins: metal, paper, and miscellaneous. Our key components include the metal detector, camera system, machine learning, and sorting mechanism. 

### Coding Guidelines

| Language   | Guideline | Tools |
|------------|-----------|-------|
| Python     |[Python Guideline](https://peps.python.org/pep-0008/)           | [Flask](https://flask.palletsprojects.com/en/2.1.x/ )     |
| JavaScript |[JavaScript Guideline](https://developer.mozilla.org/en-US/docs/MDN/Guidelines/Code_guidelines/JavaScript#general_javascript_guidelines)|       |
| CSS        |[CSS Guideline](https://developer.mozilla.org/en-US/docs/MDN/Guidelines/Code_guidelines/CSS)      |       |
| HTML       |[HTML Guideline](https://developer.mozilla.org/en-US/docs/MDN/Guidelines/Code_guidelines/HTML)      |       |


### Installation

Make sure to install all required modules prior to running with these lines of code below. Copy and paste each line into the terminal.

```pip install flask```
```pip install numpy```
```pip install cv2```
```pip install pyaudio```
```pip install audioop```

With newer versions of Python, ```pip``` may not work, you may have to use ```pip3```. 

To create our model with YOLOv5, we used this colab notebook and our dataset;
Notebook: https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov5-object-detection-on-custom-data.ipynb 
Dataset: https://universe.roboflow.com/natalie-perrochon-yqnhb/recycling-try-2 


### Usage

To run the web app via Flask, open ```website/app.py``` and run on local host port. 

To run the main object detecting function, open ```main.py``` and run. The webcam connected to the computer will take photos and run them through the algorithm. A YOLOv5 model is necessary for this code to run. 

### Acknowledgements

Authors:
Elise Ji
Jamie Kuang
Natalie Perrochon
Steven Lee

Sources:
https://docs.roboflow.com/ (API documentation)
https://flask.palletsprojects.com/en/3.0.x/quickstart/ 
https://www.youtube.com/watch?v=xIgPMguqyws&ab_channel=TechWithTim
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

Libraries Used:
Flask
PyAudio
Audioop
cv2
NumPy

Thanks!
