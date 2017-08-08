# import the necessary packages
from __future__ import division
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import sys, os
import time
from search_color import *

#search_color = PS_Search_Color()

PS_search_color = PS_Search_Color()

colorset = color2test = ['red','yellow','blue','green','white','black',]#,'black']
fn = fp = [0] * len(color2test)

for test_idx,test_color in enumerate(color2test):
    fn = 0
    fp = 0
    total_fp_test = 0
    total_fn_test = 0
    for idx,color in enumerate(colorset):

        target_folder = os.path.join('exp/color_data/test',color)


        for file in os.listdir(target_folder):
            if(file != os.path.basename("__file__")):
                if(file[-3:] == 'jpg'):

                    frame_in = cv2.imread(os.path.join(target_folder, file))
                    res = PS_search_coloㄋr.color_detection(frame_in)
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
