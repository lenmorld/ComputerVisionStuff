import cv2
import numpy as np

# sketch generating function
def sketch(image):
    # convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # clean up using Gaussian blur, reduce noise
    # http://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # extract edges
    # Canny Edge Detection uses gradient values as thresholds
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)    # change 2 thresholds based on lighting conditions
    
    # do an invert, binarize the image
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)    # pencil and paper effect
    
    return mask


# init. webcam, cap is the object provided by VideoCapture
# it contains a boolean indicating if it was successful (ret)
# and contains the iamges collected from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()                # pull image from webcam continously
    cv2.imshow('Live sketcher!', sketch(frame))
    if cv2.waitKey(1) == 13:                # enter key
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
        