import sys
import cv2
import numpy as np

#  Log system
class PS_Search_Color:

    def color_detection(self, frame_in):
        # Take each frame
        #frame = cv2.imread(image_name)
        src_height, src_width, src_channels = frame_in.shape
        roiX = int(src_width / 4)
        roiWidth = roiX * 2
        roiY = src_height / 4
        roiHeight = roiY * 2
        frame = frame_in[roiY : roiY+roiHeight, roiX : roiX+roiWidth]

        src_height, src_width, src_channels = frame.shape
        max_value = src_height * src_width * 255

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # detect red
        lower = np.array([150, 30, 30])
        upper = np.array([190, 255, 255])
        mask1 = cv2.inRange(hsv, lower, upper)
        lower = np.array([0, 30, 30])
        upper = np.array([10, 255, 255])
        mask2 = cv2.inRange(hsv, lower, upper)
        mask = mask1 + mask2
        redVal = float(mask.sum()) / float(max_value)
        if redVal > 0.4:
            red=False
        else:
            red=False

        # detect yellow
        lower = np.array([5, 100, 100])
        upper = np.array([40, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        yellowVal = float(mask.sum()) / float(max_value)
        if yellowVal > 0.15:
            yellow=True
        else:
            yellow=False

        # detect blue
        lower = np.array([100, 60, 60])
        upper = np.array([140, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        blueVal = float(mask.sum()) / float(max_value)
        if blueVal > 0.5:
            blue=True
        else:
            blue=False

        # detect green (gray)
        lower_green = np.array([103, 86, 65])
        upper_green = np.array([145, 133, 128])
        mask = cv2.inRange(hsv, lower_green, upper_green)
        greenVal = float(mask.sum()) / float(max_value)
        if greenVal > 0.01:
            green=True
        else:
            green=False

        # detect white
        lower = np.array([0, 0, 140])
        upper = np.array([256, 60, 256])
        mask = cv2.inRange(hsv, lower, upper)
        whiteVal = float(mask.sum()) / float(max_value)
        if whiteVal > 0.5:
            white=True
        else:
            white=False

        # detect black
        lower_black = np.array([110,50,50])
        upper_black= np.array([130,255,255])
        mask = cv2.inRange(hsv, lower_black, upper_black)
        blackVal = float(mask.sum()) / float(max_value)
        if blackVal > 0.15:
            black=True
        else:
            black=False

        return red, yellow, blue, green, white, black

if __name__ == "__main__":
    try:
        img_path = sys.argv[1]
    except:
        img_path = "sample.jpg"
    Search_Color = PS_Search_Color()
    img = cv2.imread(img_path)
    import time
    start_time = time.time()
    res = Search_Color.color_detection(img)
    print("--- %s seconds ---" % (time.time() - start_time))
    print res
