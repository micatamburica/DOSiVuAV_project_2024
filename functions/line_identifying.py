import numpy
import cv2
import matplotlib.pyplot as plt

def identify(Img, srcImgName = None, identified = False):
    windowSize=10
    # get histogram of the picture
    histogram = numpy.sum(Img[Img.shape[0]//2:, :], axis=0)
    
    # plt.figure(figsize=(windowSize, 6))
    # plt.plot(histogram, color='blue', label='Sum of Pixel Intensities')
    # plt.title('Histogram of Sum of Pixel Intensities (Lower Half of Image)')
    # plt.xlabel('Column Index')
    # plt.ylabel('Sum of Pixel Values')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    
    # find the middle point, left and right high peaks
    midpoint = int(histogram.shape[0]/2)
    left_base = numpy.argmax(histogram[:midpoint])
    right_base = numpy.argmax(histogram[midpoint:]) + midpoint

    # sliding Window
    y = 720
    lx = []
    ly = []
    rx = []
    ry = []
    
    
    
    
   

        
    
    
    while y > 0:
        # left
        img = Img[y-windowSize:y, left_base-50:left_base+50]
        contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"]/M["m00"])
                cy = int(M["m01"]/M["m00"])
                #lx.append(left_base-50 + cx)
                #ly.append(y-20)
                left_base = left_base-50 + cx
        
        # right
        img = Img[y-windowSize:y, right_base-50:right_base+50]
        contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"]/M["m00"])
                cy = int(M["m01"]/M["m00"])
                #rx.append(right_base-50 + cx)
                #ry.append(y-20 + cy)
                right_base = right_base-50 + cx
        
        cv2.rectangle(Img, (left_base-50,y), (left_base+50,y-windowSize), (255,255,255), 2)
        lx.append(left_base)
        ly.append(y)
        cv2.rectangle(Img, (right_base-50,y), (right_base+50,y-windowSize), (255,255,255), 2)
        rx.append(right_base)
        ry.append(y)
        y -= windowSize
    
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