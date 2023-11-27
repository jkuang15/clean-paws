from yolov5_copy.detect import run_inference
from cv2 import VideoCapture, imshow, imwrite
cam = VideoCapture(0) 


def run_paper_checker():
    confidence_average = []
    for i in range(5):
        result, image = cam.read()
        imshow("Comp_image.png", image)
        imwrite("Comp_image.png", image)
        value = run_inference()
        confidence_average.append(value)
    sum_of_list = sum(confidence_average)
    if(sum_of_list/ 5) > .05:
        #run paper motor stuff
        return True