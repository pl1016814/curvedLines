#"Curved Lines Detection" - Constantine Munoz P2, V1.0.8
#Process of code:
#Import libraries -> resize image to reduce lag -> grayscale + gaussian blur ->
#Run Hough -> Find largest out of circles -> Draw the actual circle -> Show entire image

import cv2 as cv
import numpy as np

# SETUP
img = cv.imread("Screenshot2.png")
img = cv.resize(img, (400, 200), interpolation=cv.INTER_AREA)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(img, (9, 9), 2.5)
cannyProcess = cv.Canny(gray, 135, 145)

num, labels, stats, _ = cv.connectedComponentsWithStats(cannyProcess, connectivity=8)
H = cannyProcess.shape[0]
clean = np.zeros_like(cannyProcess)
minHeight = np.zeros_like(cannyProcess)
minHeight = int(0.35 * H)
for i in range(1, num):
    x, y, w, h, area = stats[i]
    if h > minHeight:
        clean[labels == i] = 255
cannyProcess = clean

centerPoints = []
for i in range(cannyProcess.shape[0]):
    x = np.where(cannyProcess[i] > 0)[0]
    if x.size:
        xl = int(np.percentile(x, 10))
        xr = int(np.percentile(x, 90))
        if (xr - xl > 50) and (xr - xl < 275):
            centerPoints.append((int((x[0]+x[-1]) // 2), i))

for i in range(0, len(centerPoints) - 25, 25):
    cv.line(img, centerPoints[i], centerPoints[i+25], (0, 255, 0), 2)

cv.imshow("Curved Lines Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()
