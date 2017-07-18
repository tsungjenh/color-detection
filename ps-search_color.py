import os
import sys
import cv2
import numpy as np
import pylab as pl
from matplotlib.colors import hsv_to_rgb

color_boundaries_bank = {
	'red': 		([140, 30, 60],[190, 255, 255]),
	'yellow': 	([ 10, 30, 60],[ 37, 255, 255]),
	'blue':		([ 85, 30, 60],[140, 255, 255]),
	'green':	([ 37, 30, 60],[ 85, 255, 255]),
	'white':	([  0,  0,200],[179,  10, 255],[ 0, 10,200],[179, 25,255]),
	'black':	([  0,  0,  0],[179,  30, 160],[ 0, 30,  0],[179,255, 60])
}
# define base threshold, default 0.3
color_baseThreshold = {
	'red': 		0.2,
	'yellow': 	0.15,
	'blue':		0.35,
	'green':	0.01,
	'white':	0.5,
	'black':	0.01
}


#  Log system
class PS_Search_Color:

    def image_pre_analysis(self,frame_in):
	#condition = [False] * number of condition
	"""
	get which image process to apply to this frame
	"""
	return condition

    def image_process(self,frame_in,condition):

	"""
	by condition
	do white Balance
	do lamp mask
	do ...
	"""
	return frame_in

    def get_roi(self,frame_in,condition):

       	src_height, src_width, src_channels = frame_in.shape
        roiX = int(src_width / 4)
        roiWidth = roiX * 2
        roiY = src_height / 4
        roiHeight = roiY * 2
       	frame = frame_in[roiY : roiY+roiHeight, roiX : roiX+roiWidth]
	return frame


    def color_detection(self, raw_frame):

        color_to_be_detected = ['red','yellow','blue','green','white','black']

	"""
	refined_frame = self.image_process(raw_frame)
	frame = self.get_roi(refined_frame)
	"""

	src_height, src_width, src_channels = frame.shape
	max_value = src_height * src_width * 255
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        res = [False] * len(color_to_be_detected)
		# loop over all the color to be detected
        for idx,color in enumerate(color_to_be_detected):
            color_boundaries = color_boundaries_bank[color]
            assert len(color_boundaries) % 2 == 0, "Each boundary must have a lower/upper pair"

            mask = 0
            #loop over each boundary pair for this color
            for lower,upper in zip(color_boundaries[0::2], color_boundaries[1::2]):

				#detecting...
                mask = mask + cv2.inRange(hsv, np.array(lower), np.array(upper))
                Val = float(mask.sum()) / float(max_value)
                if Val > color_baseThreshold[color]:
                	res[idx] = True


        return red, yellow, blue, green, white, black


if __name__ == '__main__':

	search_color = PS_Search_Color()
	img = cv2.imread('test.jpg')
	search_color.color_detection(img)
