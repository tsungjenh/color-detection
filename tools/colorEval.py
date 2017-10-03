# import the necessary packages
from __future__ import division
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import sys, os
import time
sys.path.insert(0,'.')
from search_color import *


#search_color = PS_Search_Color()

def colorEval(base_folder,color2Eval = ['all'],search_color = Search_Color()):

	color2test = []
	colorset = ['red','yellow','blue','green','white','black',]

	if 'all' in color2Eval:
		color2test = colorset
	else:
		for color in color2set:
			if color in color2Eval:
				color2test = color2test + [color]
			else:
				print color + "'s detection not exists"

	fn = fp = [0] * len(color2test)

	for test_idx,test_color in enumerate(color2test):
    		fn = 0
    		fp = 0
    		total_fp_test = 0
    		total_fn_test = 0
    		for idx,color in enumerate(colorset):

        		target_folder = os.path.join(base_folder,color)


        		for file in os.listdir(target_folder):
            			if(file != os.path.basename("__file__")):
                			if(file[-3:] == 'jpg'):

                    				frame_in = cv2.imread(os.path.join(target_folder, file))
                    				res = search_color.color_detection(frame_in)
                    				#case: input image that is not test_color
                    				if test_idx != idx:
                        				total_fp_test += 1
                        				if res[test_idx] == True:
                            					fp += 1
                    				else: #case: input image that is test_color
                        				total_fn_test += 1
                        				if res[test_idx] == False:
                            					fn += 1
    		print("%s:" %test_color)
    		print("total_fp_test: %d fp:%d fp_rate:%f" %(total_fp_test,fp,fp/total_fp_test))
    		print("total_fn_test: %d fn:%d fn_rate:%f" %(total_fn_test,fn,fn/total_fn_test))

if __name__ == '__main__':
	base_folder = '/home/max/ironyun_proj/color-detection/exp/color_data/21'

	colorEval(base_folder)
