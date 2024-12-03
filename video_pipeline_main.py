import Functions.CameraCalibration as CamCal
import Functions.ImageProcessing as ImProc
import Functions.LaneIdentifying as LaIden
import Functions.PolynomialFitting as PolFit
import Functions.VehicleCalculations as VeCalc
import cv2

if __name__=="__main__":
    
    #input
    srcImgPath = 'test_videos/'
    srcImgName = 'challenge03.mp4'
    cap = cv2.VideoCapture(srcImgPath + srcImgName)
    
    #output will be saved if Output = True
    Output = False
    
    if Output is True:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter("output/end_" + srcImgName, fourcc, fps, (1280, 720))

    while cap.isOpened():
        
        ret, frame = cap.read()
        if not ret: break

        # 1. Distortion correction
        undistoredImg = CamCal.distortion_correction(frame)
    
        # 2. Thresholded binary image
        treshBinImg = ImProc.image_thresholding(undistoredImg)
        
        # 3. Perspective transformation 
        transformedImg = ImProc.image_perspective(treshBinImg)
        
        # 4.1. Identify lane-line pixels
        LeftX, RightX, LeftY, RightY = LaIden.lane_identifying(transformedImg)
    
        # 4.2. Fitting the polynomial
        polyImg, LeftPoly, RightPoly = PolFit.fit_polynomial(undistoredImg, LeftX, RightX, LeftY, RightY, fill=True)
        
        # 5. Determine curvature and vehicle position 
        imgWithRadius, radius = VeCalc.radius_of_curvature(undistoredImg, LeftPoly, RightPoly)
        imgWithPosition, position = VeCalc.vehicle_position(imgWithRadius, LeftPoly, RightPoly)
    
        # 6. Example video
        if Output is True:
            out.write(imgWithPosition)
        
        cv2.imshow('Cars - the movie', imgWithPosition)
        if cv2.waitKey(30) & 0xFF == 27: break

    cap.release()
    if Output is True:
        out.release()
        
    cv2.destroyAllWindows()
    