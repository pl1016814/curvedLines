#"Curved Lines Detection" - Constantine Munoz P2, V1.0.0
#Process of code:
#Import libraries -> resize image to reduce lag -> grayscale + gaussian blur ->
#Run Hough -> Find largest out of circles -> Draw the actual circle -> Show entire image

import cv2 as cv
import numpy as np

# SETUP
img = cv.imread("CurvedLines2.jpeg")
img = cv.resize(img, (300, 400), interpolation=cv.INTER_AREA)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#gaussian blur as stated in documentation doesn't work for my soda can, idk why
gray = cv.GaussianBlur(img, (7, 7), 1.5)
cannyProcess = cv.Canny(gray, 135, 145)

centerPoints = []
for i in range(cannyProcess.shape[0]):
    x = np.where(cannyProcess[i] > 0)[0]
    if x.size:
        xl = int(np.percentile(x, 10))
        xr = int(np.percentile(x, 90))
        if xr - xl > 60:
            centerPoints.append((int((x[0]+x[-1]) // 2), i))
cv.polylines(img, [np.array(centerPoints, np.int32)], False, (0, 0, 255), 2)

cv.imshow("Curved Lines Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()
