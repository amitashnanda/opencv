import numpy as np
import cv2
cap = cv2.VideoCapture('st.mp4')
while (cap.isOpened()):
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	#cv2.imshow('frame',-1)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
		cap.release()
		cv2.destroyAllWindows()