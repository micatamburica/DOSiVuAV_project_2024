import numpy
import cv2

def image_thresholding(Img, srcImgName = None):
    """
    Creates a tresholded binary image using Canny
    
    params:
        srcImgName - if given a value, 
        thresholded image will be saved in output/.

    returns:
        treshBinImg 
    """
       
    # converte image to grayscale
    gray = cv2.cvtColor(Img, cv2.COLOR_RGB2GRAY)
    
    # reduce noise
    blur = cv2.GaussianBlur(gray,(5,5), 1)
    
    # apply canny
    treshBinImg = cv2.Canny(blur, 50, 180)
    
    # save the final result if needed
    if srcImgName is not None:
        cv2.imwrite('output/thresholded_' + srcImgName, treshBinImg)
    
    return treshBinImg


def image_perspective(Img, srcImgName = None):
    """
    Changes the perspective into birds-eye view and returns it
    
    params:
        srcImgName - if given a value, 
        image with changed perspective will be saved in output/.

    returns:
        transformedImg 
    """
    
    # region of interest is handpicked with this coordinates
    topL = (560, 450)
    topR = (750, 450)
    botL = (0, 720)
    botR = (1280, 720)
    
    cord1 = numpy.float32([topL, botL, topR, botR])
    cord2 = numpy.float32([[0,0], [0,720], [1280, 0], [1280, 720]])
    
    # matrix for normal -> birds-eye
    matrix = cv2.getPerspectiveTransform(cord1, cord2)
        
    # transform perspective of an image using matrix    
    transformedImg = cv2.warpPerspective(Img, matrix, (1280, 720))
    
    # save the final result if needed
    if srcImgName is not None:
        cv2.imwrite('output/birds-eye_' + srcImgName, transformedImg)
    
    return transformedImg
    