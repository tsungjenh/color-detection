#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__        import division
import os
import sys
import cv2
import json
import numpy as np
from matplotlib.colors import hsv_to_rgb
from PIL               import Image
from importlib         import *
from image_process.auto_white_balance import auto_white_balance
from image_process.carlamp_filter     import carlamp_filter
from image_process.crop_aspect_ratio  import crop_aspect_ratio
from image_process.get_roi            import get_roi

class Search_Color:

    def __init__(self):
        """ class instance initialization """
        self.isNight     = True
        self.detect_type = 'car' #default car, option: person, human face etc...
        with open('profile/car_color_profile.json') as profile:
            self.car_profile = json.load(profile)
        with open('profile/person_color_profile.json') as profile:
            self.person_profile = json.load(profile)
        

    def color_detection(self, frame_in, detect_type = 'car'):

        status = ('night' if self.isNight else 'day')

        if detect_type == 'person':
            cur_profile = self.person_profile
            color_to_be_detected = cur_profile['color_to_be_detected']
            frame_in = crop_aspect_ratio(frame_in,True)
            frame_in = auto_white_balance(frame_in)

        elif detect_type == 'car':
            cur_profile = self.car_profile
            color_to_be_detected = cur_profile['color_to_be_detected']
            cur_profile = cur_profile[status]
            if self.isNight:
                frame_in = auto_white_balance(frame_in)



        res = [False] * len(color_to_be_detected)

        # loop over all the color to be detected



        for (idx, color) in enumerate(color_to_be_detected):


            if detect_type == 'car':

                roi_scale = cur_profile['roi_scale']

                #print roi_scale
                if self.isNight:
                    filtratio = cur_profile['filtratio'][color]
                    (frame, lightMask) = carlamp_filter(frame_in, filtratio)
                    roi_scale = roi_scale[color]
                frame = get_roi(frame, roi_scale)

                blockedPxl = sum(np.count_nonzero(e) for e in lightMask)
            else:
                frame = frame_in
                blockedPxl = 0

            (src_height, src_width, src_channels) = frame.shape
            max_value = (src_height * src_width - blockedPxl) * 255

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            color_boundaries = cur_profile['range'][color]

            assert len(color_boundaries) % 2 == 0, '[DEBUG MSG]: Each boundary must have a lower/upper pair'

            mask = 0

            # loop over each boundary pair for this color
            for (lower, upper) in zip(color_boundaries[0::2],color_boundaries[1::2]):
                # detecting...
                mask = mask + cv2.inRange(hsv, np.array(lower),np.array(upper))


            if float(max_value) != 0:
                Val = float(mask.sum()) / float(max_value)
            else:
                Val = 0

            if round(Val,2) >= cur_profile['threshold'][color]:
                res[idx] = True
        return res


if __name__ == '__main__':
    search_color = Search_Color()
    img = cv2.imread('test2.jpg')
    print search_color.color_detection(img,'car')
