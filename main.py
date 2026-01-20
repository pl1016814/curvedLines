#"Curved Lines Detection" - Constantine Munoz P2, V1.0.0
#Process of code:
#Import libraries -> resize image to reduce lag -> grayscale + gaussian blur ->
#Run Hough -> Find largest out of circles -> Draw the actual circle -> Show entire image

import cv2 as cv
import numpy as np

# SETUP
img = cv.imread("CurvedLines.jpg")
img = cv.resize(img, (512, 233), interpolation=cv.INTER_AREA)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#gaussian blur as stated in documentation doesn't work for my soda can, idk why
gray = cv.GaussianBlur(img, (7, 7), 1.5)
cannyProcess = cv.Canny(gray, 140, 150)


# turns scattered pixels into groups of lines
# a contour is an array of points/pixels
# RETR_EXTERNAL gives only OUTER contours (in rectangular box, only the outside edges)
# CHAIN_APPROX_NONE keeps all edge points
# hierarchy doesn't do anything don't worry
contours, hierarchy = cv.findContours(cannyProcess, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# contours need to be reshaped because OpenCV has an extra bracket around each point
# "-1" means it figures out the amount of rows mathematically, and "2" means it will make the array have 2 columns
points = contours[0]
# contour pixel coordinates are integers; however, linefitting needs floats instead of integers
#points = points.astype(np.float32)
for i in range(len(points)):
    cv.circle(img, (int(points[i].item(0)), int(points[i].item(1))), 2, (0, 255, 0), 2)

cv.imshow("Curved Lines Detection", cannyProcess)
cv.waitKey(0)
cv.destroyAllWindows()
