import functions.calibration_correction as correc
import functions.image_processing as procc

if __name__=="__main__":
    
    srcImgPath = 'test_images/'
    outputPath = 'output/'
    srcImgName = 'straight_lines2.jpg'
    
    # 1. Distortion correction
    undistoredImg = correc.distortion_correction(srcImgPath, srcImgName)
    
    # 2. Thresholded binary image
    treshBinImg = procc.detection(undistoredImg, srcImgName)
    
    # 3. Perspective transformation 
    procc.transformation(treshBinImg, srcImgName, True)
    