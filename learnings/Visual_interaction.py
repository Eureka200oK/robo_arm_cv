import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# The cv2.VideoCapture(0) function is used to create a video capture object that allows us to access the webcam. The argument '0' specifies that we want to use the default webcam. If you have multiple webcams, you can use '1', '2', etc. to access them.
# Or we can also use a video file instead of a webcam by providing the file path as an argument to cv2.VideoCapture().
# a while loop is used to continuously read frames from the video stream and display them in a window. The loop will run until the user presses the 'q' key to exit.
while True:
    success, img = cap.read()
    # Success is a boolean value that indicates whether the frame was successfully read from the video stream. If it is True, then img contains the captured frame. If it is False, then there was an error in reading the frame.
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Press 'q' to exit the loop
        # in the waitkey function we can use any value other than 0 , 0 -> paused , 1 -> 1ms and high frame rate , 30 -> more controlled frame rate , so this is how we can control the frame rate and broadcasting the video stream
        break