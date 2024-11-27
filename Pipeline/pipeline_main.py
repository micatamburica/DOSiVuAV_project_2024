import Calibration.calibration_correction as calib
import image_processing
import cv2
import glob

if __name__=="__main__":
    
    srcImgPath = 'test_images/'
    outputPath = 'output/'
    srcImgName = 'test6.jpg'
    
    # 1. Distortion correction
    calib.distortion_correction(srcImgPath, srcImgName)
    
    img = cv2.imread(outputPath + 'undistort_' + srcImgName)
    
    # 2. Thresholded binary image
    image_processing.detection(img, srcImgName)