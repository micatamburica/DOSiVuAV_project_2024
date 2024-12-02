def find_polynomial():
    print("TODO")
    
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
    
def fit_polynomial():
    print("TODO")