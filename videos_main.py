import Functions.CameraCalibration as correc
import Functions.ImageProcessing as procc
import Functions.line_identifying as idden
import Functions.vehicle_calculation as vehhic
import numpy
import cv2





if __name__=="__main__":
    
    cap = cv2.VideoCapture('test_videos/project_video02.mp4')
    
    prevL=None
    prevR=None
    
    while cap.isOpened():
        ret, img = cap.read()
        if not ret: break

        # 1. Distortion correction
        # load calibrated camera parameters
        calibration = numpy.load('calib.npz')
        mtx = calibration['mtx']
        dist = calibration['dist']
        rvecs = calibration['rvecs']
        tvecs = calibration['tvecs']
        
        # load one of the original distorted images
        img = cv2.resize(img, (1280, 720))
        h, w = img.shape[:2]
    
        # obtain the new camera matrix
        newcameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

        # undistort the original image
        undistortedImg = cv2.undistort(img, mtx, dist, None, newcameraMtx)
    
        # 2. Thresholded binary image
        treshBinImg = procc.detection(undistortedImg)
        
        # 3. Perspective transformation 
        transformedImg = procc.transformation(treshBinImg)
        
        # 4. Identify lane-line pixels
        

        identifiedImg, lx, rx, ly, ry = idden.identify(transformedImg)
        
       
        
        
            
        # Fit polynomial to left lane
        left_poly = numpy.polyfit(ly, lx, 2)
        plot_y = numpy.linspace(720, 450)
        left_fit_x = left_poly[0] * plot_y**2 + left_poly[1] * plot_y + left_poly[2]
        
        # Fit polynomial to right lane
        right_poly = numpy.polyfit(ry, rx, 2)
        plot_y = numpy.linspace(720, 450)
        right_fit_x = right_poly[0] * plot_y**2 + right_poly[1] * plot_y + right_poly[2]
        
        # 5. Determine curvature and vehicle position
        img = cv2.resize(img, (1280, 720))
        h, w = img.shape[:2]
    
        # obtain the new camera matrix
        newcameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

        # undistort the original image
        undistortedImg = cv2.undistort(img, mtx, dist, None, newcameraMtx)
        round_left, round_right, round_avg = vehhic.radiusOfCurvature(undistortedImg, left_poly, right_poly)
        resul = vehhic.curv_pos(undistortedImg,left_poly,right_poly)
        
        # Draw the polynomial line
        left_points = numpy.array([numpy.transpose(numpy.vstack([left_fit_x, plot_y]))], dtype=numpy.int32)
        cv2.polylines(undistortedImg, left_points, isClosed=False, color=(0, 0, 160), thickness=4)  # Red
        right_points = numpy.array([numpy.transpose(numpy.vstack([right_fit_x, plot_y]))], dtype=numpy.int32)
        cv2.polylines(undistortedImg, right_points, isClosed=False, color=(0, 0, 160), thickness=4)  # Red
        
        text2 = 'Position : ' + str(resul)
        cv2.putText(undistortedImg, text2, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)
        text3 = 'Average Curvature : ' + str(round_avg)
        cv2.putText(undistortedImg, text3, (50,150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)

        cv2.imshow('Cars', undistortedImg)
        
        if cv2.waitKey(30) & 0xFF == 27: break

    cap.release()
    cv2.destroyAllWindows()
    