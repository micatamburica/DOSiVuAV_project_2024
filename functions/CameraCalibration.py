import cv2
import numpy
import glob

def distortion_correction(originalImg, srcImgName = None):
    """
    Corrects the distortion of a given image and returns it
    
    params:
        srcImgName - if given a value, 
        undistorted image will be saved in output/, 
        as well as the side by side of distorted and undistorted.

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
    Img = cv2.resize(originalImg, (1280, 720))
    h, w = Img.shape[:2]
 
    # obtain the new camera matrix
    newcameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

    # undistort the original image
    undistortedImg = cv2.undistort(Img, mtx, dist, None, newcameraMtx)
    
    # save the final result if needed
    if srcImgName is not None:
        cv2.imwrite('output/undistorted_' + srcImgName, undistortedImg)
        cv2.imwrite('output/sbys_' + srcImgName, numpy.hstack((Img, undistortedImg)))
        
    return undistortedImg


def run_chessboard_calibration(srcImgPath, NumRows, NumColumns):
    """
    Calibrates camera using a set of chessboard images, saves the result in calib.npz.

    returns:
        none
    """
    
    # termination criteria for finding the chessboard 
    criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 30, 0.001)
    
    # prepare object points, 3-axis (x,y,z) like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0) and scale 
    objp = numpy.zeros((NumRows * NumColumns, 3), numpy.float32)
    objp[:,:2] = numpy.mgrid[0:NumRows, 0:NumColumns].T.reshape(-1,2)

    objpoints = [] # 3d points in real world space
    imgpoints = [] # 2d points in image plane

    # for every image in the camera_cal/
    images = glob.glob(srcImgPath + '*.jpg')
    
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        # find the chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, (NumRows, NumColumns), None)
    
        # if found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
    
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)
    
    # find the calibration values of the camera  
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    
    # save them in calib.npz
    numpy.savez('calib.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
