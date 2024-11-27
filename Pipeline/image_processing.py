import numpy
import cv2

def detection(Img, srcImgName):
    
    # converte image to grayscale
    gray = cv2.cvtColor(Img, cv2.COLOR_RGB2GRAY)
    
    # reduce noise
    blur = cv2.GaussianBlur(gray,(5,5), 0)
    
    # apply canny
    canny = cv2.Canny(blur, 50, 180)
    
    cv2.imwrite('output/canny_' + srcImgName, canny)
    cv2.waitKey(0)