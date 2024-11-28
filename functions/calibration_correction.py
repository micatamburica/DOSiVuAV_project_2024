import cv2
import numpy

def distortion_correction(srcImgPath, srcImgName, undistort = False, side_by_side = False):
    """
    Corrects the distortion of a given image and returns it
    
    params:
        undistort = False (automatic)
        undistort = True (if you want undistorted image saved as output)
    
        side_by_side = False (automatic)
        side_by_side = True (if you want a side by side saved as output)

    returns:
        undistortedImg 
    """
    
    # load calibrated camera parameters
    calibration = numpy.load('calib.npz')
    mtx = calibration['mtx']
    dist = calibration['dist']
    rvecs = calibration['rvecs']
    tvecs = calibration['tvecs']
    
    # load one of the original distorted images
    Img = cv2.imread(srcImgPath + srcImgName)
    h, w = Img.shape[:2]
 
    # obtain the new camera matrix
    newcameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

    # undistort the original image
    undistortedImg = cv2.undistort(Img, mtx, dist, None, newcameraMtx)
    
    # save the final result if needed
    if(undistort):
        cv2.imwrite('output/undistort_' + srcImgName, undistortedImg)
    
    if(side_by_side):
        cv2.imwrite('output/SbyS_undistort_' + srcImgName, numpy.hstack((Img, undistortedImg)))
        
    return undistortedImg
