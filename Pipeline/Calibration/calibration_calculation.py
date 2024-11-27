import numpy
import cv2
import glob

def run_chessboard_calibration(srcImgPath, NumRows, NumColumns):
    """
    Calibrates camera using a set of chessboard images

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
    
        '''
            # draw and display the corners
            cv2.drawChessboardCorners(img, (NumRows, NumColumns), corners2, ret)
            cv2.imshow('Image with found corners', img)
            
        else:
        
            cv2.imshow('Image where corners were not found', img)
            
        cv2.waitKey(0)
        '''
          
    # calibrate the camera     
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    
    # saving them in calib.npz
    numpy.savez('calib.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
