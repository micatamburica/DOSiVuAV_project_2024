import functions.calibration_calculation as calcul
import functions.calibration_correction as correc

if __name__=="__main__":
    
    # real life physical measures
    NUM_ROWS = 6
    NUM_COLUMNS = 9
    
    srcImgPath = 'camera_cal/'
    
    # getting the calibration values
    calcul.run_chessboard_calibration(srcImgPath, NUM_ROWS, NUM_COLUMNS)
    
    # example of distortion correction
    correc.distortion_correction(srcImgPath, 'calibration2.jpg')
    correc.distortion_correction(srcImgPath, 'calibration3.jpg', True)
    correc.distortion_correction(srcImgPath, 'calibration4.jpg', False, True)
    