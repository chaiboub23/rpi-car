# **Documentation**

### Camera Module

This module is for get the image from the camera.

import picamera module and time module

```python
import time
import picamera
```

Make a function for catching the image, so the opencv module can get the information from it later

```python
def get():
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 24
        time.sleep(2)
        image = np.empty((240 * 320 * 3,), dtype=np.uint8)
        camera.capture(image, 'bgr')
        image = image.reshape((240, 320, 3))
        return image
```

*Notice that the image is in "bgr", if you want to make it into "rbg", you can inverse the list using [::1]*

------



### Color picker code

This module is using for the opencv to test what range of the color it should take in.

import cv2 and numpy

```python
import cv2
import numpy as np
```

Make the image into black and white. Set the basic variables and making the trackbar, so you can adjust and decide in what range the color should be detected

```python
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty(a):
    pass


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

cap = cv2.VideoCapture('last.h264')
frameCounter = 0

while True:
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0

    success, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
```

*The function empty is for the trackbar, all it need to do is "pass"*

Put on the video that you want to test on.

```python
cap = cv2.VideoCapture('last.h264')
frameCounter = 0
```

Making a loop and get the value from the adjusting 

```python
while True:
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0

    success, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
```

Set the initial value and show the image

```python
lower = np.array([80, 0, 0])
    upper = np.array([255, 160, 255])
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

------



### Utlis module

import opencv and numpy

```python
import cv2
import numpy as np
```

The thresholding function is for making the image black and white. Here is the place that you will put your color picker value in for "*lowerwhite*" and "*upperwhite*".

It will return the **white lane**.

```python
def thresholding(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#HSV
    #RANGE of color
    lowerWhite = np.array([70, 0, 150])
    upperWhite = np.array([255, 255, 255])##NEED TO ADJUST USING COLORPICKER
    maskWhite = cv2.inRange(imgHsv, lowerWhite, upperWhite)
    return maskWhite
```

The warpimg function will drag the image flat. It will set four point to form a trapezoidal and drag the image warping parallel to the screen. 

It will return the image after **warping**.

```python
def warpImg(img,points,w,h,inv=False):#inv=inverse
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inv:
        matrix=cv2.getPerspectiveTransform(pts2,pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp
```

Here is the **trackbar** that you can adjust your four point with. It will give you a trackbar, read your input and return those value.

```python
#for the trackbars
def nothing(a):
    pass

#trackbars
def initializeTrackbars(intialTracbarVals,wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT,nothing)

#get value for each
def valTrackbars(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points
```

After get the value from the trackbar, here is the code that it will **draw the point** on the image. It will return a image with four point drew on.

```python
def drawPoints(img,points):
    for x in range( 0,4):
        cv2.circle(img,(int(points[x][0]),int(points[x][1])),15,(0,0,255),cv2.FILLED)#make four points
    return img
```

*Things that you can change: The "15" refers to the **size**, and the "(0,0,255)" refers to the **color** of the point*



This function will return **the base point** **of the lane**. It subtract the average of pixels from numbers of pixels of the center line, we will **get the curve** in that way.

```python
def getHistogram(img,minPer=0.1,display=False,region=1):
    if region==1:
        histValues = np.sum(img, axis=0)# an array of all the sum of pixels in each column
    else:
        histValues = np.sum(img[img.shape[0]//region::], axis=0)#sum of pixels in a particular region
    #find what is our path, what are noises
    maxValue = np.max(histValues)  # FIND THE MAX VALUE
    minValue = minPer * maxValue #what is not considered as our path, what we should ignore
    indexArray = np.where(histValues >= minValue)  # ALL INDICES WITH MIN VALUE OR ABOVE
    basePoint = int(np.average(indexArray))  # AVERAGE ALL MAX INDICES VALUES,find the center point
    #print(basePoint)
    if display:
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(histValues):
            cv2.line(imgHist, (x, img.shape[0]),(x,img.shape[0]-intensity // 255//region), (255,0,255), 1)#show the line as a purple line
            cv2.circle(imgHist, (basePoint, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)#show the basepoint as a yellow ball
        return basePoint,imgHist
    return basePoint
```

The final function is for **stack all the image together**, so when we are going to adjust the points or the color, we can see it clearly and it won't run in a mess.

```python
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
```

------



### Lane Detect module

This is the module combine all the information above and will actually detect the lane.



import the modules, including the utlis module. 

*Notice, do not spell wrong*

```python
import cv2
import numpy as np
import utlis
```

Put basic information

```python
curvelist=[]#curve value
avgVal=10#average value for list for curvelist
```

Input image in this function and set the basic information

*display=0:nothing*

*display=1: just the result (with the curve)*

*display=2:all the things (including the trackbar and image)*

```python
def getLaneCurve(img,display=2):
    imgCopy=img.copy()
    imgResult=img.copy()
    imgThres = utlis.thresholding(img)#output image

    hT,wT,c=img.shape
    points = utlis.valTrackbars()
    imgWarp= utlis.warpImg(imgThres,points,wT,hT)#output warped image with black and white
    imgWarpPoints=utlis.drawPoints(imgCopy,points)
```

Path the midpoint

```python
midPoint,imgHist=utlis.getHistogram(imgWarp,display=True,minPer=0.5,region=4)
```

*region=1/4, means the bottom 1/4 are being counted*

*minPer=0.5,means minimum Percent,make too small numbers do not consider as a part of our path*



Basepoint, get our curve value

```python
curveAveragePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minPer=0.9)#region=1
curveRaw=curveAveragePoint-midPoint#our curve value
```

Make path value list

```python
curvelist.append(curveRaw)
if len(curvelist)>avgVal:
    curvelist.pop(0)
curve=int(sum(curvelist)/len(curvelist))
```

Display

```python
if display != 0:
    imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
    imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
    imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
    imgLaneColor = np.zeros_like(img)
    imgLaneColor[:] = 0, 255, 0
    imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
    imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
    midY = 450
    cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
    cv2.line(imgResult, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
    cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
    for x in range(-30, 30):
        w = wT // 20
        cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
                 (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
    #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    #cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3);
#stuck all the image together
if display == 2:
    imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgWarp],
                                         [imgHist, imgLaneColor, imgResult]))
    cv2.imshow('ImageStack', imgStacked)
elif display == 1:
    cv2.imshow('Resutlt', imgResult)
```

You can also test individually use these codes

```python
#test individually
#cv2.imshow('Thres',imgThres)
#cv2.imshow('Warp', imgWarp)
#cv2.imshow('Warp Points', imgWarpPoints)
#cv2.imshow('Histogram', imgHist)
```

normalization, use positive, negative and "0" to determine whether it is a left curve or right or straight.

```python
curve=curve//100
if curve>-1:
    curve=1
if curve<-1:
    curve=-1
print(curve)
return curve
```

return the curve value and end the function.



Set the test video here and set the points position here, use trackbar to adjust.

```python
if __name__ == '__main__':
    cap = cv2.VideoCapture('last.h264')
    #put the points value in
    intialTracbarVals = [60, 200, 0, 255]##NEED TO ADJUST use trackbars!
    utlis.initializeTrackbars(intialTracbarVals)
```

Make a loop so the adjusting will be much easier. 

```python
frameCounter=0 #for the loop

while True:
    #looping for Warped img
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0

    success, img = cap.read() # GET THE IMAGE
    img = cv2.resize(img,(480,240)) # RESIZE
    getLaneCurve(img)#
    #curve=getLaneCurve(img,display=0/1/2)only result/trackbars/everything
    cv2.imshow('Vid',img)# SHOW THE VIDEO
    #wait user
    cv2.waitKey(1)
```

------



### Hardware implement

import the module we need, pay attention to the spelling

```python
from LaneDetect import getLaneCurve
import cam
import explorerhat
```

the function main is for responding the curve.

**You may need to change the sensitivity after testing.**

```python
def main():
    img = cam.get()
    curveVal = getLaneCurve(img, 1)

    sen = 1.3  # SENSITIVITY
    if curveVal==1:
        explorerhat.motor.stop()
        explorerhat.motor.one.forwards(0.20* sen)
        explorerhat.motor.two.forwards(0.20)
    elif curveVal==-1:
        explorerhat.motor.stop()
        explorerhat.motor.two.forwards(0.20* sen)
        explorerhat.motor.one.forwards(0.20)
    elif curveVal==0:
        explorerhat.motor.stop()
        explorerhat.motor.forwards(0.20)
    else:
        explorerhat.motor.stop()
    # cv2.waitKey(1)
```

Loop it

```python
if __name__ == '__main__':
    while True:
        main()
```