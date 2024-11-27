import cv2
import numpy

def distortion_correction(srcImgPath, srcImgName, Mtx, Dist):
    """
    Corrects the distortion of a given image and saves the result 

    returns:
        none
    """
    
    # load one of the original distorted images as an example
    Img = cv2.imread(srcImgPath + srcImgName)
    h, w = Img.shape[:2]
 
    # obtain the new camera matrix
    newcameraMtx, roi = cv2.getOptimalNewCameraMatrix(Mtx, Dist, (w, h), 1, (w, h))

    # undistort the original image
    undistortedImg = cv2.undistort(Img, Mtx, Dist, None, newcameraMtx)
    
    # save the final result example
    cv2.imwrite('Result_' + srcImgName, numpy.hstack((Img, undistortedImg)))
    cv2.waitKey(0)
