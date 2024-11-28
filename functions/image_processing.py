import numpy
import cv2

def detection(Img, srcImgName, binary = False):
    """
    Creates a tresholded binary image using canny
    
    params:
        binary = False (automatic)
        binary = True (if you want tresholded binary image saved as output)

    returns:
        treshBinImg 
    """
    
    # converte image to grayscale
    gray = cv2.cvtColor(Img, cv2.COLOR_RGB2GRAY)
    
    # reduce noise
    blur = cv2.GaussianBlur(gray,(5,5), 0)
    
    # apply canny
    treshBinImg = cv2.Canny(blur, 50, 180)
    
    # save the final result if needed
    if(binary):
        cv2.imwrite('output/binary_' + srcImgName, treshBinImg)
    
    return treshBinImg