import Calibration.calibration_correction as calib

if __name__=="__main__":
    
    srcImgPath = 'test_images/'
    
    calib.distortion_correction(srcImgPath, 'whiteCarLaneSwitch.jpg', True)