#! python3

# Use hand gestures to scroll

import cv2
import numpy as np
import pyautogui

print("About to run capture")
cap = cv2.VideoCapture()
print("Just finished running capture")

if cap:
	print("CAPTURE")
else:
	print("NO CAPTURE")

yellow_lower = np.array([22,93,0])
yellow_upper = np.array([45,255,255])
prev_y = 0

while True:
	ret, frame = cap.read()
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	for c in contours:
		area = cv2.contourArea(c)
		
