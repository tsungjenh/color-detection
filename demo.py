from search_color import Search_Color
import os
import cv2

if __name__ == '__main__':
    color_to_be_tested = ["red","black","yellow","blue","green","white"]
    target_folder = 'data/car/21'
    search_color = Search_Color()
    for idx, color in enumerate(color_to_be_tested):
        print '------------------------------' + color
        for file in os.listdir(os.path.join(target_folder,color)):
            if(file != os.path.basename("__file__")):
                if(file[-3:] == 'jpg'):
                    img_path   = os.path.join(target_folder,color,file)
                    origin_img = cv2.imread(img_path)
                    res = search_color.color_detection(origin_img,'car')
                    print img_path,res
