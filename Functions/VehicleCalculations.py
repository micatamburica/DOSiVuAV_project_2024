import numpy

def radiusOfCurvature(Img, left_fit, right_fit):
    
    ym_per_pix = 0.015
    
    y_eval = Img.shape[0]/2
    # left_radius = ((1 + (2*left_fit[0]*y_eval + left_fit[1])**2)**1.5) / (2*left_fit[0])
    # right_radius = ((1 + (2*right_fit[0]*y_eval + right_fit[1])**2)**1.5) / (2*right_fit[0])
    left_curverad = ((1 + (2*left_fit[0]*y_eval*ym_per_pix + left_fit[1])**2)**1.5) / numpy.absolute(2*left_fit[0])
    right_curverad = ((1 + (2*right_fit[0]*y_eval*ym_per_pix + right_fit[1])**2)**1.5) / numpy.absolute(2*right_fit[0])
    avg_radius = (left_curverad+right_curverad)/2
    
    return round(left_curverad,2), round(right_curverad,2), round(avg_radius,2)
    

def curv_pos(img, l_fit, r_fit):

    # Define conversions in x and y from pixels space to meters
    ym_per_pix = 3.048/100 # meters per pixel in y dimension, lane line is 10 ft = 3.048 meters
    xm_per_pix = 0.0019#3.7/378 # meters per pixel in x dimension, lane width is 12 ft = 3.7 meters
    left_curverad, right_curverad, center_dist = (0, 0, 0)
    # Define y-value where we want radius of curvature
    # I'll choose the maximum y-value, corresponding to the bottom of the image
    h = img.shape[0]
    ploty = numpy.linspace(0, h-1, h)
    y_eval = numpy.max(ploty)
  
    # Identify the x and y positions of all nonzero pixels in the image
    nonzero = img.nonzero()
    nonzeroy = numpy.array(nonzero[0])
    nonzerox = numpy.array(nonzero[1])
    # Again, extract left and right line pixel positions
    # leftx = nonzerox[l_lane_inds]
    # lefty = nonzeroy[l_lane_inds] 
    # rightx = nonzerox[r_lane_inds]
    # righty = nonzeroy[r_lane_inds]
    
    # if len(leftx) != 0 and len(rightx) != 0:
    #     # Fit new polynomials to x,y in world space
    #     left_fit_cr = np.polyfit(lefty*ym_per_pix, leftx*xm_per_pix, 2)
    #     right_fit_cr = np.polyfit(righty*ym_per_pix, rightx*xm_per_pix, 2)
    #     # Calculate the new radii of curvature
    #     left_curverad = ((1 + (2*left_fit_cr[0]*y_eval*ym_per_pix + left_fit_cr[1])**2)**1.5) / np.absolute(2*left_fit_cr[0])
    #     right_curverad = ((1 + (2*right_fit_cr[0]*y_eval*ym_per_pix + right_fit_cr[1])**2)**1.5) / np.absolute(2*right_fit_cr[0])
    #     # Now our radius of curvature is in meters
    
    # Distance from center is image x midpoint - mean of l_fit and r_fit intercepts 
    if r_fit is not None and l_fit is not None:
        car_position = img.shape[1]/2
        l_fit_x_int = l_fit[0]*h**2 + l_fit[1]*h + l_fit[2]
        r_fit_x_int = r_fit[0]*h**2 + r_fit[1]*h + r_fit[2]
        lane_center_position = (r_fit_x_int + l_fit_x_int) /2
        center_dist = (car_position - lane_center_position) * xm_per_pix
    return numpy.absolute(center_dist)


    #lane_center_position = (r_fit_x_int + l_fit_x_int) /2 center_dist = (car_position - lane_center_position) * x_meters_per_pix
    
    
