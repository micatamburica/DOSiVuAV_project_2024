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
    blur = cv2.GaussianBlur(gray,(5,5), 1)
    
    # apply canny
    treshBinImg = cv2.Canny(blur, 50, 180)
    
    # save the final result if needed
    if(binary):
        cv2.imwrite('output/binary_' + srcImgName, treshBinImg)
    
    return treshBinImg

def transformation(Img, srcImgName, transform = False):
    """
    Changes the perspective into bird-eye view and returns it
    
    params:
        transform = False (automatic)
        transform = True (if you want transformed image saved as output)

    returns:
        transformedImg 
    """
    
    topL = (570, 450)
    topR = (730, 450)
    botL = (30, 700)
    botR = (1250, 700)
    
    cord1 = numpy.float32([topL, botL, topR, botR])
    cord2 = numpy.float32([[0,0], [0,720], [1280, 0], [1280, 720]])
    
    matrix = cv2.getPerspectiveTransform(cord1, cord2)
    transformedImg = cv2.warpPerspective(Img, matrix, (1280, 720))
    
    # save the final result if needed
    if(transform):
        cv2.imwrite('output/transformed_' + srcImgName, transformedImg)
    
    return transformedImg
    