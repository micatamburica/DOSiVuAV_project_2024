import calibration_calculation
import example_correction

if __name__=="__main__":
    
    # real life physical measures
    NUM_ROWS = 6
    NUM_COLUMNS = 9
    
    srcImgPath = 'camera_cal/'
    srcImgName = 'calibration4.jpg'
    
    Mtx, Dist = calibration_calculation.run_chessboard_calibration(srcImgPath, NUM_ROWS, NUM_COLUMNS)
    example_correction.distortion_correction(srcImgPath, srcImgName, Mtx, Dist)
    