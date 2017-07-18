#white balance
import numpy as np
from PIL import Image
import sys

def inRange(img, lower_b, upper_b):
    ch1, ch2, ch3 = cv2.split(img)
    ch1m = (lower_b[0] <= ch1) & (ch1 <= upper_b[0])
    ch2m = (lower_b[1] <= ch2) & (ch2 <= upper_b[1])
    ch3m = (lower_b[2] <= ch3) & (ch3 <= upper_b[2])
    mask = ch1m & ch2m & ch3m
    return mask.astype(np.uint8)*255

def imgFilt(img):

    filtered_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    grimg = cv2.cvtColor(filtered_img,cv2.COLOR_BGR2GRAY)

    hsvimg = cv2.cvtColor(filtered_img,cv2.COLOR_BGR2HSV)

    lightMask = np.asarray(grimg)
    Mask_indices = lightMask > 150
    filtered_img[Mask_indices] =255
    return filtered_img

def imgHsvFilt(img):

    filtered_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    #grimg = cv2.cvtColor(filtered_img,cv2.COLOR_BGR2GRAY)

    hsvimg = cv2.cvtColor(filtered_img,cv2.COLOR_BGR2HSV)

    lightMask = np.asarray(hsvimg)
    Mask_indices = lightMask > 150
    filtered_img[Mask_indices] =255
    return filtered_img

def from_pil(pimg):
    pimg = pimg.convert(mode='RGB')
    nimg = np.asarray(pimg)
    nimg.flags.writeable = True
    return nimg

def to_pil(nimg):

    #return Image.fromarray(np.uint8(nimg))
    rgb_nimg = Image.fromarray(np.uint8(nimg)).convert('RGB')
    opencv_img = np.array(rgb_nimg)
    # Convert RGB to BGR
    opencv_img = opencv_img[:, :, ::-1].copy()
    return opencv_img

def retinex(nimg):
    nimg = nimg.transpose(2, 0, 1).astype(np.uint32)
    mu_g = nimg[1].max()
    nimg[0] = np.minimum(nimg[0]*(mu_g/float(nimg[0].max())),255)
    nimg[2] = np.minimum(nimg[2]*(mu_g/float(nimg[2].max())),255)
    return nimg.transpose(1, 2, 0).astype(np.uint8)

def retinex_adjust(nimg):
    """
    from 'Combining Gray World and Retinex Theory for Automatic White Balance in Digital Photography'
    """
    nimg = nimg.transpose(2, 0, 1).astype(np.uint32)
    sum_r = np.sum(nimg[0])
    sum_r2 = np.sum(nimg[0]**2)
    max_r = nimg[0].max()
    max_r2 = max_r**2
    sum_g = np.sum(nimg[1])
    max_g = nimg[1].max()
    coefficient = np.linalg.solve(np.array([[sum_r2,sum_r],[max_r2,max_r]]),
                                  np.array([sum_g,max_g]))

    nimg[0] = np.minimum((nimg[0]**2)*coefficient[0] + nimg[0]*coefficient[1],255)
    sum_b = np.sum(nimg[1])
    sum_b2 = np.sum(nimg[1]**2)
    max_b = nimg[1].max()
    max_b2 = max_r**2
    coefficient = np.linalg.solve(np.array([[sum_b2,sum_b],[max_b2,max_b]]),
                                             np.array([sum_g,max_g]))
    nimg[1] = np.minimum((nimg[1]**2)*coefficient[0] + nimg[1]*coefficient[1],255)
    return nimg.transpose(1, 2, 0).astype(np.uint8)
