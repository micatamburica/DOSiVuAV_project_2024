import numpy
import cv2

def radius_of_curvature(Img, left_poly, right_poly):
    """
    Calculates the radius of curvature

    returns:
       imgWithRadius, center_radius
    """    
    
    y_per_pix = 3/100       # meters per pixel in y dimension
    
    # current position of the vehicle [y]
    y_eval = Img.shape[0]/2
    
    # R = (1 + (2*A*x + B)^2)^3/2 / |2*A|
    left_radius = ((1 + (2 * left_poly[0] * y_eval * y_per_pix  + left_poly[1])**2)**1.5) / numpy.absolute(2 * left_poly[0])
    right_radius = ((1 + (2 * right_poly[0] * y_eval * y_per_pix + right_poly[1])**2)**1.5) / numpy.absolute(2 * right_poly[0])
    
    # radius of curvature of vehicle with respect to center
    center_radius = (left_radius + right_radius) / 2
    
    # write in the text onto the picture
    text = 'Average Curvature : ' + str(numpy.round(center_radius)) + ' [m]'
    cv2.putText(Img, text, (50,100), cv2.FONT_HERSHEY_DUPLEX, 0.7, (200, 200, 200), 1, cv2.LINE_AA)

    return Img, center_radius


def vehicle_position(Img, left_poly, right_poly):
    """
    Calculates the vehicle position with respect to center

    returns:
       imgWithPosition, vehicle_position
    """

    x_per_pix = 3.7/900     # meters per pixel in x dimension

    # current position of the vehicle [y]
    y_eval = Img.shape[0]

    # position of the left and right lane 
    left_position = left_poly[0] * y_eval**2 + left_poly[1] * y_eval + left_poly[2]
    right_position = right_poly[0] * y_eval**2 + right_poly[1] * y_eval + right_poly[2] 

    # position of the center of the lane
    center_position = (left_position + right_position) / 2

    # it is assumed that the vehicle is placed in the center of the picture
    # if value is negative, vehicle is left to the center of the lane, othervise right
    vehicle = ((Img.shape[1]//2) - center_position) * x_per_pix
    
    # write in the text onto the picture
    text = 'Position : ' + str(numpy.absolute(numpy.round(vehicle, 3))) + ' [m]'
    if(vehicle > 0):
        text += ' (to the right)'    
    if(vehicle < 0):
        text += ' (to the left)'
    cv2.putText(Img, text, (50,130), cv2.FONT_HERSHEY_DUPLEX, 0.7, (200, 200, 200), 1, cv2.LINE_AA)

    return Img, vehicle
