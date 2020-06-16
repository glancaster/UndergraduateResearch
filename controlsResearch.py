import control as c
import matplotlib.pyplot as plt 
import numpy as np 
import cv2 as cv

cam = cv.VideoCapture(1)
cam.set(3,800)
cam.set(4,800)
ret, frame1 = cam.read()
ret, frame2 = cam.read()

while cam.isOpened():
    diff = cv.absdiff(frame1,frame2)
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5),0)
    _, thresh = cv.threshold(blur, 20,255,cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours,_ = cv.findContours(dilated,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = cv.boundingRect(contour)
        if cv.contourArea(contour) <700:
            continue
        cv.rectangle(frame1, (x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(frame1, "status: {}".format('movement'),(10,20), cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    #cv.drawContours(frame1,contours,-1,(0,255,0),2)

    cv.imshow('Video',frame1)
    frame1 = frame2
    ret,frame2 = cam.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
