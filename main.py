import cv2
import numpy as np
from LaneDetector import LaneDetector
 
from moviepy.editor import *
#detector = LaneDetector()

#clip = VideoFileClip('video_1.avi')
#processed = clip.fl_image(detector.process)
#processed.write_videofile('video_1_a.mp4', audio=False)
detector = LaneDetector()
cap = cv2.VideoCapture('video_2.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    image = detector.process(frame)

    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()