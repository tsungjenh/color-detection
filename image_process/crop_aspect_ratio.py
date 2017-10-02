import cv2



def crop_aspect_ratio(img, isUpper, aspect_ratio = 0.5):


    src_height, src_width, src_channels = img.shape

    roix_upper = int(src_width * 0.25)
    roix_upper_width = int(src_width * aspect_ratio)
    roiy_upper = int(src_height * 0.15)
    roiy_upper_width = int(src_height * 0.35)

    cropped_img = img[ roiy_upper: roiy_upper + roiy_upper_width,roix_upper: roix_upper + roix_upper_width]


    return cropped_img
