from search_color import Search_Color
import os
import cv2

if __name__ == '__main__':
    target_folder = 'exp/color_data/facial/'
    search_color = Search_Color()
    color_to_be_tested = ['lightskin']
    for idx, color in enumerate(color_to_be_tested):
        for file in os.listdir(target_folder + color):
            if(file != os.path.basename("__file__")):
                if(file[-3:] == 'jpg'):
                    origin_img = cv2.imread(target_folder + color + '/' + file)
                    print file, search_color.color_detection(origin_img,'facial')[0],search_color.color_detection(origin_img,'facial')[1]
