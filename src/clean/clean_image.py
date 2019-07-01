import numpy as np
import cv2


def inpaint(path_to_img, path_to_mask):
    """Take image and mask, ipaint in masked area and return cleared image"""
    img = cv2.imread(path_to_img)
    mask = cv2.imread(path_to_mask,0)
    return cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)


path_to_img = 'orig.jpg'
path_to_mask = 'mask.jpg'
save_as = "masked.jpg"

cv2.imwrite(save_as, inpaint(path_to_img, path_to_mask))
