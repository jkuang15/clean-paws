# program to capture single image from webcam in python 
  
# importing OpenCV library 
from cv2 import VideoCapture, imshow, imwrite
from image_detect import compare_image
import time
import metal
from paper_confidence_checker import run_paper_checker

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

        imshow("Comp_image.png", image) 
        imwrite("Comp_image.png", image)
        

        pixels = compare_image()

        if pixels > 3:

            if metal.run_mic() is True:
                print('METAL')
            elif run_paper_checker() is True:
                print('PAPER')
            else:
                print('MISC')





            # destroyWindow("GeeksForGeeks") 



        else: 
        #waits 5 seconds if nothing is detected before going on w the loop
            print("nawr")
            time.sleep(5)

        
    else:
        print("No Change Detected")
        


 


  
# # If captured image is corrupted, moving to else part 
# else: 
#     print("No image detected. Please! try again")
