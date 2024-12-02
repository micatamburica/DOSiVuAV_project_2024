import Functions.CameraCalibration as CamCal
import Functions.ImageProcessing as ImProc
import Functions.LaneIdentifying as LaIden
import Functions.PolynomialFitting as PolFit
import Functions.VehicleCalculations as VeCalc
import cv2

if __name__=="__main__":
    
    srcImgPath = 'test_images/'
    srcImgName = 'solidYellowCurve2.jpg'
    
    originalImg = cv2.imread(srcImgPath + srcImgName)
    
    # 1. Distortion correction
    undistoredImg = CamCal.distortion_correction(originalImg)
    
    # 2. Thresholded binary image
    treshBinImg = ImProc.image_thresholding(undistoredImg)
    
    # 3. Perspective transformation 
    transformedImg = ImProc.image_perspective(treshBinImg)
   
    # 4.1. Identify lane-line pixels
    LeftX, RightX, LeftY, RightY = LaIden.lane_identifying(transformedImg)
    
    # 4.2. Fitting the polynomial
    polyImg, LeftPoly, RightPoly = PolFit.fit_polynomial(undistoredImg, LeftX, RightX, LeftY, RightY)
    
'''
    
    # 5. Determine curvature and vehicle position
    undistoredImg = CamCal.distortion_correction(originalImg)
    round_left, round_right, round_avg = vehhic.radiusOfCurvature(undistoredImg, left_poly, right_poly)
    
    text2 = 'Left Curvature : ' + str(round_left) + ', Right Curvature : ' + str(round_right)
    cv2.putText(undistoredImg, text2, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)
    text3 = 'Average Curvature : ' + str(round_avg)
    cv2.putText(undistoredImg, text3, (50,150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)
    
    vehhic.curv_pos(undistoredImg,left_poly,right_poly)
    
    
    cv2.imshow("Lane Detection - Sliding Windows", undistoredImg)
    
    cv2.waitKey(0)
'''