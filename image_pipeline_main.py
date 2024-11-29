import Functions.CameraCalibration as CamCal
import Functions.image_processing as procc
import Functions.line_identifying as idden
import Functions.vehicle_calculation as vehhic
import numpy
import cv2

if __name__=="__main__":
    
    srcImgPath = 'test_images/'
    srcImgName = 'solidYellowCurve2.jpg'
    
    originalImg = cv2.imread(srcImgPath + srcImgName)
    
    # 1. Distortion correction
    undistoredImg = CamCal.distortion_correction(originalImg)

'''
    # 2. Thresholded binary image
    treshBinImg = procc.detection(undistoredImg, srcImgName)
    
    # 3. Perspective transformation 
    transformedImg = procc.transformation(treshBinImg, srcImgName, True)
    
    # 4. Identify lane-line pixels
    identifiedImg, lx, rx, ly, ry = idden.identify(transformedImg, srcImgName)
    
    # Fit polynomial to left lane
    left_poly = numpy.polyfit(ly, lx, 2)
    plot_y = numpy.linspace(720, 450)
    left_fit_x = left_poly[0] * plot_y**2 + left_poly[1] * plot_y + left_poly[2]
    
    # Fit polynomial to right lane
    right_poly = numpy.polyfit(ry, rx, 2)
    plot_y = numpy.linspace(720, 450)
    right_fit_x = right_poly[0] * plot_y**2 + right_poly[1] * plot_y + right_poly[2]
    
    # 5. Determine curvature and vehicle position
    undistoredImg = CamCal.distortion_correction(originalImg)
    round_left, round_right, round_avg = vehhic.radiusOfCurvature(undistoredImg, left_poly, right_poly)
    
    # Draw the polynomial line
    left_points = numpy.array([numpy.transpose(numpy.vstack([left_fit_x, plot_y]))], dtype=numpy.int32)
    cv2.polylines(undistoredImg, left_points, isClosed=False, color=(0, 0, 255), thickness=5)  # Red
    right_points = numpy.array([numpy.transpose(numpy.vstack([right_fit_x, plot_y]))], dtype=numpy.int32)
    cv2.polylines(undistoredImg, right_points, isClosed=False, color=(0, 0, 255), thickness=5)  # Red
    
    text2 = 'Left Curvature : ' + str(round_left) + ', Right Curvature : ' + str(round_right)
    cv2.putText(undistoredImg, text2, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)
    text3 = 'Average Curvature : ' + str(round_avg)
    cv2.putText(undistoredImg, text3, (50,150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)
    
    vehhic.curv_pos(undistoredImg,left_poly,right_poly)
    
    
    cv2.imshow("Lane Detection - Sliding Windows", undistoredImg)
    
    cv2.waitKey(0)
'''