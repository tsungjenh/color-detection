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

def colorEval(base_folder, detect_type = 'car', color2Eval = ['all'], search_color = Search_Color()):
    color2test = []
    colorset = ["red","black","yellow","blue","green","white"]

    if 'all' in color2Eval:
        color2test = colorset
    else:
        for color in colorset:
            if color in color2Eval:
                color2test = color2test + [color]
            else:
                print "[DEBUG MSG]: %s + 's detector not exists" % color
    fn = fp = [0] * len(color2test)

    for test_color in color2test:
        fn = 0
        fp = 0
        total_fp_test = 0
        total_fn_test = 0
        for idx, color in enumerate(colorset):

            target_folder = os.path.join(base_folder, color)

            for file in os.listdir(target_folder):
                if(file != os.path.basename("__file__")):
                    if(file[-3:] == 'jpg'):
                        frame_in = cv2.imread(os.path.join(target_folder,file))
                        res = search_color.color_detection(frame_in, detect_type)

                        res_arr = res.split(',')

                        test_idx = colorset.index(test_color)
                        if test_color != color:
                            total_fp_test += 1
                            if test_color in res_arr:
                                fp += 1
                        else:
                            total_fn_test += 1
                            if test_color not in res_arr:

                                fn += 1



        print("%s:" %test_color)
        print("total_fp_test: %d fp:%d fp_rate:%f" %(total_fp_test,fp,fp/total_fp_test))
        print("total_fn_test: %d fn:%d fn_rate:%f" %(total_fn_test,fn,fn/total_fn_test))

if __name__ == '__main__':
    base_folder = 'data/color_data/12'
    colorEval(base_folder,'car')
