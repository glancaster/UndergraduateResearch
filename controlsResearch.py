import numpy as np 
import cv2 as cv

cam = cv.VideoCapture(1)
_,cap = cam.read()

while cam.isOpened():
    _,cap = cam.read()
    gray = cv.cvtColor(cap,cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT,1.2,500)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
	        cv.circle(cap, (x, y), r, (0, 255, 0), 2)
            
        cv.rectangle(cap, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        cv.imshow("output", cap)
        
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()






















'''
cam = cv.VideoCapture(0)
cam.set(3,800)
cam.set(4,800)
ret, frame1 = cam.read()
ret, frame2 = cam.read()
'''
'''
#color tracking
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([69,255,255])
    upper_blue = np.array([150,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
'''

'''
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
        cv.circle(frame1, (x,y),(x+w),(0,255,0),2)
        cv.putText(frame1, "status: {}".format('movement'),(10,20), cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    #cv.drawContours(frame1,contours,-1,(0,255,0),2)

    cv.imshow('Video',frame1)
    frame1 = frame2
    ret,frame2 = cam.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
'''
'''
cap = cv.VideoCapture(0)
# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0,255,(100,3))
# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
while(1):
    ret,frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new, good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv.add(frame,mask)
    cv.imshow('frame',img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)
'''