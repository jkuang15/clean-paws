import torch
import numpy as np
import cv2
from time import time

class PaperDetection:
    """
    Class that will implement yolov5 model to maker inferences on camera
    """

    def __init__(self, capture_index, model_name):
        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available else 'cpu'
        print("using device: ", self.device)

    def get_video_capture(self):
        """
        creates new video streaming object and uses it to 
        make predicitons
        """
        return cv2.VideoCapture(self.capture_index)
    
    def load_model(self, model_name):
        """
        Loads the yolov5 model from pytorch hub
        """
        model_path = "Users/stevenl/yolov5/yolov5/runs/train/yolov5s_results5/weights/best.pt"
        if model_name:
            model = torch.hub.load('ultralytics/yolov5', 'custom', path = model_name, force_reload = True)
        return model

    
