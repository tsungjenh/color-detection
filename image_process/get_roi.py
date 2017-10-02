import cv2

def get_roi(frame_in, roi_scale):
    """ return region of interest for color detection """
    """
    if isNight:
        roi_scale = color_profile['night']['roi_scale'][color]
    else:
        roi_scale = color_profile['day']['roi_scale']
    """
    roiWid = 10
    roiEdg = roi_scale

    (src_height, src_width, src_channels) = frame_in.shape

    roiX = int(src_width / roiWid)
    roiWidth = roiX * roiEdg
    roiY = int(src_height / roiWid)
    roiHeight = roiY * roiEdg

    frame = frame_in[roiY:int(roiY + roiHeight), roiX:int(roiX + roiWidth)]


    return frame
