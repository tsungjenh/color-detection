import cv2
import numpy as np
from matplotlib import pyplot as plt




img = cv2.imread('./redlight1.jpg')

img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imshow("images", np.hstack([img, dst]))
cv2.waitKey(0)