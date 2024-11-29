import Functions.CameraCalibration as CamCal
import cv2

if __name__=="__main__":
    
    # real life physical measures
    NUM_ROWS = 6
    NUM_COLUMNS = 9
    
    srcImgPath = 'camera_cal/'
    srcImgName = 'calibration4.jpg'
    
    # getting the calibration values (calib.npz)
    CamCal.run_chessboard_calibration(srcImgPath, NUM_ROWS, NUM_COLUMNS)
    
    # example of distortion correction
    originalImg = cv2.imread(srcImgPath + srcImgName)
    
    CamCal.distortion_correction(originalImg)
    CamCal.distortion_correction(originalImg, srcImgName)
    