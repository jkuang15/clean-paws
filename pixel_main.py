# program to capture single image from webcam in python 
  
# importing OpenCV library 
from cv2 import VideoCapture, imshow, waitKey, imwrite, destroyWindow
from pixel_func import compare_image
import time

# initialize the camera 
# If you have multiple camera connected with  
# current device, assign a value in cam_port  
# variable according to that 
cam = VideoCapture(0) 
  
# # reading the input using the camera 

# #saving to variable

trigger = True

while trigger == True:
    
# # reading the input using the camera 

    result, image = cam.read() 


# If image will detected without any error,  
# show result

    if result: 
        
        # showing result and saving image in local storage 

        imshow("GeeksforGeeks", image) 
        imwrite("GeeksforGeeks.png", image)
        

        pixels = compare_image()

        if pixels > 3:

            print("Call Main Func")
            # destroyWindow("GeeksForGeeks") 

            trigger = False
            break

        

        else: 
        #waits 5 seconds if nothing is detected before going on w the loop
            print("nawr")
            time.sleep(5)

        
    else:
        print("No image detected")
        


 


  
# # If captured image is corrupted, moving to else part 
# else: 
#     print("No image detected. Please! try again")
