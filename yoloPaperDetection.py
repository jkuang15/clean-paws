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
        if model_name:
            model = torch.hub.load('yolov5/', 'custom', path='Users/stevenl/yolov5/yolov5/runs/train/weights/best.pt', source='local') 
        return model

    def score_frame(self, frame):
        """
        Takes a single fram as the input and uses the yolov5 model
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord
    
    def class_to_label(self, x):
        return self.classes[int(x)]
    
    def plot_boxes(self, results, frame):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2,y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
        
        return frame

    def __call__(self):
        player = self.get_video_capture()
        assert player.isOpened()

        while True:
            start_time = time()
            ret, frame = player.read()
            frame = cv2.resize(frame, (416,416))

            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)
            end_time = time()
            cv2.imshow('YOLOv5 Detection', frame)

            if cv2.waitKey(5) & 0xFF == 27:
                break
        player.release()

detector = PaperDetection(capture_index=0, model_name='best.pt')
detector()
