import cv2
import numpy as np
from LaneDetector import LaneDetector
 
from moviepy.editor import *
detector = LaneDetector()

clip = VideoFileClip('challenge.mp4')
processed = clip.fl_image(detector.process)
processed.write_videofile('challengeoutput.mp4', audio=False)