import numpy
import cv2

def lane_identifying(Img, srcImgName = None):
    """
    Identify lane-line pixels using the sliding window technique
    
    params:
        srcImgName - if given a value, 
        image with sliding window will be saved in output/.

    returns:
        LeftX, RightX, LeftY, RightY 
    """
    
    windowSize = 10
    windowWidth = 50
    Y = 720
    
    copyImg = Img.copy()
    
    # get histogram of the picture
    histogramVal = numpy.sum(Img[Img.shape[0]//2:, :], axis=0)

    # find the middle point, left and right high peaks
    midpoint = int(histogramVal.shape[0]/2)
    left_base = numpy.argmax(histogramVal[:midpoint])
    right_base = numpy.argmax(histogramVal[midpoint:]) + midpoint

    # list to save coordinates
    LeftX = []
    LeftY = []
    RightX = []
    RightY = []
    
    # starting from bottom of the picture (720 pix) and moving up by window size (10 pix)
    while Y > 0:
        
        # left lane
        img = copyImg[Y-windowSize:Y, left_base-windowWidth:left_base+windowWidth]
        contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"]/M["m00"])
                left_base = left_base - windowWidth + cx
        
        # right lane
        img = copyImg[Y-windowSize:Y, right_base-windowWidth:right_base+windowWidth]
        contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"]/M["m00"])
                right_base = right_base - windowWidth + cx
        
        # save the results as rectangles on the picture, and as coordinates
        cv2.rectangle(copyImg, (left_base-windowWidth, Y), (left_base+windowWidth, Y-windowSize), (255,255,255), 2)
        LeftX.append(left_base)
        LeftY.append(Y)
        cv2.rectangle(copyImg, (right_base-windowWidth, Y), (right_base+windowWidth, Y-windowSize), (255,255,255), 2)
        RightX.append(right_base)
        RightY.append(Y)
        
        Y -= windowSize
    
    # save the final result if needed
    if srcImgName is not None:
        cv2.imwrite('output/identified_' + srcImgName, copyImg)
        
    return LeftX, RightX, LeftY, RightY
    