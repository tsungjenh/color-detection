from search_color import Search_Color
import os
import cv2

if __name__ == '__main__':
    color_to_be_tested = ["red","yellow","black","blue","green","white"]
    target_folder = 'data/car/21'
    search_color = Search_Color()
    for idx, color in enumerate(color_to_be_tested):
        for file in os.listdir(os.path.join(target_folder,color)):
            if(file != os.path.basename("__file__")):
                if(file[-3:] == 'jpg'):
                    origin_img = cv2.imread(target_folder + color + '/' + file)
                    res = search_color.color_detection(origin_img,'car')
                    print res