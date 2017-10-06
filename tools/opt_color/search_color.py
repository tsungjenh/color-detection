import sys
import cv2
import numpy as np
sys.path.insert(0,'/home/max/ironyun_proj/color-detection/image_process')
from auto_white_balance import auto_white_balance
from crop_aspect_ratio import crop_aspect_ratio
from get_roi import get_roi

class Search_Color:

    def color_detection(self, frame_in, color2opt, roiScale, filtratio, color_param, detect_type = 'car'):

        if detect_type == 'person':
            frame_in = crop_aspect_ratio(frame_in,True)

        frame_in = auto_white_balance(frame_in)

        roiWid = 10
        roiEdg = roiScale

        src_height, src_width, src_channels = frame_in.shape

        roiX = int(src_width / roiWid)
        roiWidth = int(roiX * roiEdg)
        roiY = int(src_height / roiWid)
        roiHeight = int(roiY * roiEdg)

        frame = frame_in#[roiY : roiY+roiHeight, roiX : roiX+roiWidth]

        if detect_type == 'car':
            frame,lightMask = imgFilt(frame,filtratio)
            blockedPxl = sum(np.count_nonzero(e) for e in lightMask)
        else:
            blockedPxl = 0

        src_height, src_width, src_channels = frame.shape

        max_value = ((src_height*src_width)-blockedPxl)*255

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        if color2opt is 'white':
            lower = np.array([0,0, color_param[0]])
            upper = np.array([179, color_param[1], 255])
            mask = cv2.inRange(hsv, lower, upper)
            lower = np.array([0,color_param[1], color_param[2]])
            upper = np.array([179, color_param[3], 255])
            mask = mask + cv2.inRange(hsv, lower, upper)

        elif color2opt is 'black':
            lower = np.array([0,0,0])
            upper = np.array([179,color_param[0],color_param[1]])
            mask  = cv2.inRange(hsv,lower,upper)
            lower = np.array([0,color_param[0],0])
            upper = np.array([179,255,color_param[2]])
            mask  = mask + cv2.inRange(hsv, lower, upper)
        elif color2opt in ['lightskin']:
            lower = np.array([0, color_param[0],color_param[1]])
            upper = np.array([color_param[2],color_param[3],255])
            mask  = cv2.inRange(hsv,lower,upper)

        elif color2opt in ['darkskin']:
            lower = np.array([0, color_param[0],0])
            upper = np.array([color_param[1],color_param[2],color_param[3]])
            mask  = cv2.inRange(hsv,lower,upper)

        else: #others
            lower = np.array([color_param[0],color_param[1], color_param[2]])
            upper = np.array([color_param[3], 255, 255])
            mask = cv2.inRange(hsv, lower, upper)

        if(float(max_value) != 0):
            Val = float(mask.sum()) / float(max_value)
        else:
            Val = 0

        res = round(Val,2)


        return res
