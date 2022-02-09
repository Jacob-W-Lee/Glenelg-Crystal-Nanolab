# code adapted from https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
# program to capture single image from webcam in python

# importing libraries
import numpy
import cv2
import time

# initialize the camera If you have multiple camera connected with current device, assign a value in cam_port variable according to that
cam_port = 0
cam = cv2.VideoCapture(cam_port)

# repeat 32 times (0-31 inclusive)
dayCounter = 0
while dayCounter <= 31:

    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:
        # showing result, it take frame name and image output
        # update image name based on day
        imageName = "day" + str(dayCounter)
        cv2.imshow(imageName, image)

        #Get file name from image name
        fileName = imageName + ".png"

        # saving image in local storage
        cv2.imwrite(fileName, image)

        # Wait 2 seconds change this to 1 day (86400000) for actual experiment
        cv2.waitKey(2000)

        # Close the image
        cv2.destroyAllWindows()

    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
    dayCounter += 1
