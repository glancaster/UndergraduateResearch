# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

# lower and upper boundaries of the "green" in HSV
greenLower = (20, 80, 100)
greenUpper = (60, 255, 255)

# initialize the list of tracked points, to draw the ball trajectory
pts = deque(maxlen=args["buffer"])
vx = []

# if a video path was not supplied, use the webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])

# infinite loop
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	start = time.time()
	for i in range(0,2): 
		ret,frame = camera.read()
	end = time.time()
	seconds = end - start
	fps = 2/ seconds
	fps2 = str(fps)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame,fps2,(10,450), font, 1,(255,255,255),1,cv2.LINE_AA)
	#print(fps)


	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
		break

	# resize the frame, blur it, and convert it to the HSV color space
	frame = imutils.resize(frame, width=600, height= 600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

			z = 548.394657*(21.335/radius)

			#print(z)
			

		

	# update the points queue
	pts.appendleft(center)

	# loop over the set of tracked points
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue

		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (100, 0, 100), thickness)
	
	
		
		#vx = abs((pts[i-1][0]-pts[i][0])/(start-end))
		#v.append(vx)
		#print(sum(v[-30:])/30)
		#print(pts[i][0])

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	# cv2.imshow("Frame", mask)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
