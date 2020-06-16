import control as c
import matplotlib.pyplot as plt 
import numpy as np 
import cv2 as cv

cam = cv.VideoCapture(0)
cam.set(3,800)
cam.set(4,800)

while True:
    success, img = cam.read()
    cv.imshow('Video',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
