import cv2
import numpy as numpy

# cap = cv2.VideoCapture(0)			# where 0 is default cam

# cap = cv2.VideoCapture("/home/me/my.avi")			# video file

# WORKS
# cap = cv2.VideoCapture("rtsp://mpv.cdn3.bigCDN.com:554/bigCDN/definst/mp4:bigbuckbunnyiphone_400.mp4")

# WORKS
cap = cv2.VideoCapture("http://cemrcam1.cemr.wvu.edu/nphMotionJpeg?resolution=640x480&.mjpg")


# cap = cv2.VideoCapture('../images/walking.avi')

# cap.open("http://dummy.url?stream=mpeg"); // a mjpeg , ipcam stream

while cap.isOpened():
	ret, frame = cap.read()

	cv2.imshow("STREAM", frame)

	if cv2.waitKey(1) == 13:
		break