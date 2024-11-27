import cv2
import numpy

def distortion_correction(srcImgPath, srcImgName, side_by_side = False):
    """
    Corrects the distortion of a given image and saves the result
    
    params:
        side_by_side = True 
            - if you want a side by side of distorted and undistorted image
        side_by side = False
            - if you want only undistorted image as output

    returns:
        none
    """
    # load calibrated camera parameters
    calibration = numpy.load('Calibration/calib.npz')
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
    
    # save the final result example
    cv2.imwrite('output/undistort_' + srcImgName, undistortedImg)
    
    if(side_by_side):
        cv2.imwrite('output/side_by_side_' + srcImgName, numpy.hstack((Img, undistortedImg)))
