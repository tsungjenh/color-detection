import sys
import cv2
import numpy as np

#  Log system        
class PS_Search_Color:

	def color_detection(self, frame_in):
		# Take each frame
		#frame = cv2.imread(image_name)
		src_height, src_width, src_channels = frame_in.shape
		roiX = int(src_width / 4)
		roiWidth = roiX * 2
		roiY = src_height / 4
		roiHeight = roiY * 2
		frame = frame_in[roiY : roiY+roiHeight, roiX : roiX+roiWidth]
		
		src_height, src_width, src_channels = frame.shape
		max_value = src_height * src_width * 255
		
		# Convert BGR to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		# detect red
		lower = np.array([150, 30, 30])
		upper = np.array([190, 255, 255])
		mask1 = cv2.inRange(hsv, lower, upper)
		lower = np.array([0, 30, 30])
		upper = np.array([10, 255, 255])
		mask2 = cv2.inRange(hsv, lower, upper)
		mask = mask1 + mask2
		redVal = float(mask.sum()) / float(max_value)
		if redVal > 0.2:
			red="true"
		else:
			red="false"
		
		# detect yellow
		lower = np.array([5, 100, 100])
		upper = np.array([40, 255, 255])
		mask = cv2.inRange(hsv, lower, upper)
		yellowVal = float(mask.sum()) / float(max_value)
		if yellowVal > 0.15:
			yellow="true"
		else:
			yellow="false"

		# detect blue
		lower = np.array([100, 60, 60])
		upper = np.array([140, 255, 255])
		mask = cv2.inRange(hsv, lower, upper)
		blueVal = float(mask.sum()) / float(max_value)
		if blueVal > 0.35:
			blue="true"
		else:
			blue="false"

		# detect green (gray)
		lower_green = np.array([103, 86, 65])
		upper_green = np.array([145, 133, 128])
		mask = cv2.inRange(hsv, lower_green, upper_green)
		greenVal = float(mask.sum()) / float(max_value)
		if greenVal > 0.01:
			green="true"
		else:
			green="false"

		# detect white
		lower = np.array([0, 0, 140])
		upper = np.array([256, 60, 256])
		mask = cv2.inRange(hsv, lower, upper)
		whiteVal = float(mask.sum()) / float(max_value)
		if whiteVal > 0.5:
			white="true"
		else:
			white="false"

		# detect black
		lower_black = np.array([110,50,50])
		upper_black= np.array([130,255,255])
		mask = cv2.inRange(hsv, lower_black, upper_black)
		blackVal = float(mask.sum()) / float(max_value)
		if blackVal > 0.01:
			black="true"
		else:
			black="false"
		
		return red, yellow, blue, green, white, black
		
	def color_detection_rgb(self, frame):
		# Take each frame
		#frame = cv2.imread(image_name)
		src_height, src_width, src_channels = frame.shape
		max_value = src_height * src_width * 255
		
		# Convert BGR to HSV
		#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		hsv = frame
		
		# detect red
		lower_red = np.array([17, 15, 100])
		upper_red = np.array([50, 56, 200])
		mask = cv2.inRange(hsv, lower_red, upper_red)
		red = float(mask.sum()) / float(max_value)

		# detect yellow
		lower_yellow = np.array([25, 146, 190])
		upper_yellow = np.array([62, 174, 250])
		mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
		yellow = float(mask.sum()) / float(max_value)

		# detect blue
		lower_blue = np.array([86, 31, 4])
		upper_blue = np.array([220, 88, 50])
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		blue = float(mask.sum()) / float(max_value)

		# detect green (gray)
		#lower_green = np.array([103, 86, 65])
		#upper_green = np.array([145, 133, 128])
		#mask = cv2.inRange(hsv, lower_green, upper_green)
		#green = float(mask.sum()) / float(max_value)

		# detect white
		lower_white = np.array([103, 86, 65])
		upper_white = np.array([145, 133, 128])
		mask = cv2.inRange(hsv, lower_white, upper_white)
		white = float(mask.sum()) / float(max_value)

		# detect black
		#lower_blue = np.array([110,50,50])
		#upper_blue = np.array([130,255,255])
		#mask = cv2.inRange(hsv, lower_blue, upper_blue)
		#blue = float(mask.sum()) / float(max_value)
		
		return red, yellow, blue, float(0), white, float(0)
