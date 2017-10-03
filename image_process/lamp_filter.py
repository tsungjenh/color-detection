import cv2
import numpy as np
def lamp_filter(frame, filtratio):
    """ car lamp filter to remove negative light effect on color detection """
    ratio = filtratio * 255
    # filtered_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # hsvimg = cv2.cvtColor(filtered_img,cv2.COLOR_BGR2HSV)
    lightMask = np.asarray(gray_frame)
    Mask_indices = lightMask > ratio
    frame[Mask_indices] = 255
    return (frame, Mask_indices)
