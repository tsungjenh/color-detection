#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import cv2
import numpy as np
from matplotlib.colors import hsv_to_rgb
from PIL import Image
from color_profile import color_profile


class PS_Search_Color:

    def isNight(self, arg):

                # alg to detect night or day

        return arg

    def imgFilt(self, img, color):
        filtratio = color_profile['night']['filtratio'][color]
        ratio = filtratio * 255

                # filtered_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

        filtered_img = img
        grimg = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2GRAY)

                # hsvimg = cv2.cvtColor(filtered_img,cv2.COLOR_BGR2HSV)

        lightMask = np.asarray(grimg)
        Mask_indices = lightMask > ratio
        filtered_img[Mask_indices] = 255
        return (filtered_img, Mask_indices)

    def white_balance(self, frame_in):

                # Gray World Plus Retinex Theory for Automatic White Balance

        pimg = cv2.cvtColor(frame_in, cv2.COLOR_BGR2RGB)
        pimg = Image.fromarray(pimg)
        pimg = pimg.convert(mode='RGB')
        nimg = np.asarray(pimg)
        nimg.flags.writeable = True

        nimg = nimg.transpose(2, 0, 1).astype(np.uint32)
        mu_g = nimg[1].max()
        nimg[0] = np.minimum(nimg[0] * (mu_g / float(nimg[0].max())),255)
        nimg[2] = np.minimum(nimg[2] * (mu_g / float(nimg[2].max())),255)
        nimg = nimg.transpose(1, 2, 0).astype(np.uint8)

        nimg = nimg.transpose(2, 0, 1).astype(np.uint32)
        sum_r = np.sum(nimg[0])
        sum_r2 = np.sum(nimg[0] ** 2)
        max_r = nimg[0].max()
        max_r2 = max_r ** 2
        sum_g = np.sum(nimg[1])
        max_g = nimg[1].max()
        coefficient = np.linalg.solve(np.array([[sum_r2, sum_r], [max_r2, max_r]]), np.array([sum_g, max_g]))

        nimg[0] = np.minimum(nimg[0] ** 2 * coefficient[0] + nimg[0] * coefficient[1], 255)
        sum_b = np.sum(nimg[1])
        sum_b2 = np.sum(nimg[1] ** 2)
        max_b = nimg[1].max()
        max_b2 = max_r ** 2
        coefficient = np.linalg.solve(np.array([[sum_b2, sum_b],[max_b2, max_b]]), np.array([sum_g, max_g]))
        nimg[1] = np.minimum(nimg[1] ** 2 * coefficient[0] + nimg[1] * coefficient[1], 255)

        nimg = nimg.transpose(1, 2, 0).astype(np.uint8)

        rgb_nimg = Image.fromarray(np.uint8(nimg)).convert('RGB')
        opencv_img = np.array(rgb_nimg)
        opencv_img = opencv_img[:, :, ::-1].copy()

        return opencv_img

    def get_roi(self,frame_in,isNight,color):

        if isNight:
            roi_scale = color_profile['night']['roi_scale'][color]
        else:
            roi_scale = color_profile['day']['roi_scale']

        roiWid = 10
        roiEdg = roi_scale

        (src_height, src_width, src_channels) = frame_in.shape

        roiX = int(src_width / roiWid)
        roiWidth = roiX * roiEdg
        roiY = int(src_height / roiWid)
        roiHeight = roiY * roiEdg

        frame = frame_in[roiY:roiY + roiHeight, roiX:roiX + roiWidth]
        return frame

    def color_detection(self, frame_in):

        color_to_be_detected = ['red','yellow','blue','green','white','black']

        res = [False] * len(color_to_be_detected)

                # loop over all the color to be detected

        for (idx, color) in enumerate(color_to_be_detected):

            isNight = self.isNight(True)
            status = ('night' if isNight else 'day')

            if isNight:
                frame_in = self.white_balance(frame_in)

            frame = self.get_roi(frame_in, isNight, color)
            (frame, lightMask) = self.imgFilt(frame, color)

            (src_height, src_width, src_channels) = frame.shape
            blockedPxl = sum(np.count_nonzero(e) for e in lightMask)
            max_value = (src_height * src_width - blockedPxl) * 255


            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            color_boundaries = color_profile[status]['range'][color]

            assert len(color_boundaries) % 2 == 0, 'Each boundary must have a lower/upper pair'

            mask = 0

            # loop over each boundary pair for this color
            for (lower, upper) in zip(color_boundaries[0::2],color_boundaries[1::2]):

                # detecting...
                mask = mask + cv2.inRange(hsv, np.array(lower),np.array(upper))
                if float(max_value) != 0:
                    Val = float(mask.sum()) / float(max_value)
                else:
                    Val = 0
                if Val > color_profile[status]['threshold'][color]:
                    res[idx] = True

        return res


if __name__ == '__main__':

    search_color = PS_Search_Color()
    img = cv2.imread('test.jpg')
    search_color.color_detection(img)
