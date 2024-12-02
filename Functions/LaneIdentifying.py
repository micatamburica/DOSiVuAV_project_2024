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
    
'''
    # Fit polynomial to left lane
    left_poly = numpy.polyfit(ly, lx, 2)
    plot_y = numpy.linspace(0, 720, num=720)
    left_fit_x = left_poly[0] * plot_y**2 + left_poly[1] * plot_y + left_poly[2]
    
    # Fit polynomial to right lane
    right_poly = numpy.polyfit(ry, rx, 2)
    plot_y = numpy.linspace(0, 720, num=720)
    right_fit_x = right_poly[0] * plot_y**2 + right_poly[1] * plot_y + right_poly[2]
    
     
    #convert back to not black and white
    identifiedImg = cv2.cvtColor(Img, cv2.COLOR_GRAY2BGR)

    # Draw the polynomial line
    # left_points = numpy.array([numpy.transpose(numpy.vstack([left_fit_x, plot_y]))], dtype=numpy.int32)
    # cv2.polylines(identifiedImg, left_points, isClosed=False, color=(0, 0, 255), thickness=5)  # Red
    # right_points = numpy.array([numpy.transpose(numpy.vstack([right_fit_x, plot_y]))], dtype=numpy.int32)
    # cv2.polylines(identifiedImg, right_points, isClosed=False, color=(0, 0, 255), thickness=5)  # Red

    # cv2.imshow("Lane Detection - Sliding Windows", identifiedImg)
    # cv2.waitKey(0)
    
    topL = (560, 450)
    topR = (750, 450)
    botL = (0, 720)
    botR = (1280, 720)
    
    cord1 = numpy.float32([topL, botL, topR, botR])
    cord2 = numpy.float32([[0,0], [0,720], [1280, 0], [1280, 720]])
    
    matrix = cv2.getPerspectiveTransform(cord2, cord1)

    # Transform the coordinates back to the original perspective
    birdseye_coords = numpy.array(list(zip(lx, ly)), dtype='float32').reshape(-1, 1, 2)
    original_coords_left = cv2.perspectiveTransform(birdseye_coords, matrix)

    # Extract x and y coordinates and convert to lists
    original_lx = original_coords_left[:, 0, 0].tolist()
    original_ly = original_coords_left[:, 0, 1].tolist()
    
    birdseye_coords = numpy.array(list(zip(rx, ry)), dtype='float32').reshape(-1, 1, 2)
    original_coords_right = cv2.perspectiveTransform(birdseye_coords, matrix)
    
    # Extract x and y coordinates and convert to lists
    original_rx = original_coords_right[:, 0, 0].tolist()
    original_ry = original_coords_right[:, 0, 1].tolist()
      
    return identifiedImg, original_lx, original_rx, original_ly, original_ry
    
'''