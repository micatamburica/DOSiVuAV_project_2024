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
    polyImg, LeftPoly, RightPoly = PolFit.fit_polynomial(undistoredImg, LeftX, RightX, LeftY, RightY, fill=False)
    
    # 5. Determine curvature and vehicle position 
    imgWithRadius, radius = VeCalc.radius_of_curvature(undistoredImg, LeftPoly, RightPoly)
    imgWithPosition, position = VeCalc.vehicle_position(imgWithRadius, LeftPoly, RightPoly)
    
    # 6. Example image
    cv2.imshow("Example Image " + srcImgName, imgWithPosition)
    cv2.waitKey(0)