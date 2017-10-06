from config import *
import os
import cv2
import sys
from search_color import Search_Color
#search_color = PS_Search_Color()

search_color = Search_Color()
def sample_color(threshold, roiScale, filtratio, color_param, color2opt):

    clr_idx = colorset.index(color2opt)

    this_color_count = 0
    fp = 0
    fn = 0
    #ps_count = 0
    total = 0
    for idx, color in enumerate(color_to_be_tested):
        for file in os.listdir(target_folder + color):
            if(file != os.path.basename("__file__")):
                if(file[-3:] == 'jpg'):

                    origin_img = cv2.imread(target_folder + color + '/' + file)

                    res = search_color.color_detection(origin_img, color2opt, roiScale, filtratio, color_param, 'person')

                    total += 1

                    if res>=threshold and clr_idx != idx:
                        fp = fp +1
                    elif clr_idx == idx:
                        this_color_count += 1
                        if res<threshold:
                            fn = fn + 1

    return total,this_color_count,fp,fn
