import numpy
import cv2

def fit_polynomial(Img, LeftX, RightX, LeftY, RightY, srcImgName = None, fill = False):
    """
    Finds the polynomial and draws it on the image
    
    params:
        srcImgName - if given a value, 
        image with polynomial will be saved in output/. 
        fill - if given True, 
        area of the lane will be filled in.

    returns:
        polynomialImg, left_fit_x, right_fit_x
    """    

    # fit to left lane
    left_poly = numpy.polyfit(LeftY, LeftX, 2)      # find A, B, C
    plot_y = numpy.linspace(0, 720, num=720)        # array of 720
    left_fit_x = left_poly[0] * plot_y**2 + left_poly[1] * plot_y + left_poly[2]        # y = A*x^2 + B*x + C
   
    # fit to right lane
    right_poly = numpy.polyfit(RightY, RightX, 2)   # find A, B, C
    plot_y = numpy.linspace(0, 720, num=720)        # array of 720
    right_fit_x = right_poly[0] * plot_y**2 + right_poly[1] * plot_y + right_poly[2]    # y = A*x^2 + B*x + C
    
    # region of interest 
    topL = (560, 450)
    topR = (750, 450)
    botL = (0, 720)
    botR = (1280, 720)
    
    cord1 = numpy.float32([topL, botL, topR, botR])
    cord2 = numpy.float32([[0,0], [0,720], [1280, 0], [1280, 720]])
    
    # birds-eye -> matrix for normal
    matrix = cv2.getPerspectiveTransform(cord2, cord1)

    # transform the Left coordinates back to the original perspective
    birdseye_coords = numpy.array(list(zip(left_fit_x, plot_y)), dtype='float32').reshape(-1, 1, 2)
    original_coords_left = cv2.perspectiveTransform(birdseye_coords, matrix)

    # extract x and y Left coordinates and convert to lists
    original_LeftX = original_coords_left[:, 0, 0].tolist()
    original_LeftY = original_coords_left[:, 0, 1].tolist()
    
    # transform the Right coordinates back to the original perspective
    birdseye_coords = numpy.array(list(zip(right_fit_x, plot_y)), dtype='float32').reshape(-1, 1, 2)
    original_coords_right = cv2.perspectiveTransform(birdseye_coords, matrix)
    
    # extract x and y Right coordinates and convert to lists
    original_RightX = original_coords_right[:, 0, 0].tolist()
    original_RightY = original_coords_right[:, 0, 1].tolist()
    
    # fill in the area
    if fill is True:
        corners = numpy.array([[original_RightX[0], original_RightY[0]], [original_LeftX[0], original_LeftY[0]], [original_LeftX[719], original_LeftY[719]], [original_RightX[719], original_RightY[719]]], dtype=numpy.int32)
        cv2.fillPoly(Img, [corners], (130, 180, 0, 120))

    # draw the polynomial line
    left_points = numpy.array([numpy.transpose(numpy.vstack([original_LeftX, original_LeftY]))], dtype=numpy.int32)
    cv2.polylines(Img, left_points, isClosed=False, color=(0, 0, 150), thickness=4)  # left - red
    right_points = numpy.array([numpy.transpose(numpy.vstack([original_RightX, original_RightY]))], dtype=numpy.int32)
    cv2.polylines(Img, right_points, isClosed=False, color=(150, 0, 0), thickness=4)  # right - blue
    
    # save the final result if needed
    if srcImgName is not None:
        cv2.imwrite('output/poly_' + srcImgName, Img)
        
    return Img, left_poly, right_poly
