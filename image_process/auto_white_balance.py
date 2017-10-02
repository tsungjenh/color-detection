#white balance
import numpy as np
from PIL import Image
import sys
import cv2

def auto_white_balance(frame_in):
    """ Gray World Plus Retinex Theory for Automatic White Balance """
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
    awb_img = np.array(rgb_nimg)
    awb_img = awb_img[:, :, ::-1].copy()

    return awb_img
