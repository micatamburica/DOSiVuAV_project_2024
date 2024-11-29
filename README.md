**LANE FINDING PROJECT**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

---

### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

Geometric camera calibration is a process in which parameters of a lens and image sensor of an image or video camera are estimated. Usually cameras distort the image, which makes the image unreliable to measure real life measures that are shown in the image. 
To combat this, first we take a set of sample images that have a pattern such as chessboard (makes it easy to find 2D coordinates), find the 3D real world points (object points) and the corresponding 2D coordinates of these points in the image (image points). These values are then used in the calibration process, that assumes a pinhole camera model. In this model, a 3D point in the world coordinate system is projected onto the 2D image plane by a simple linear transformation. The output values of camera calibration are: Camera matrix, Distortion coefficients, Rotation vectors, Translation vectors. This step should be done only one time, after that the values are saved in calib.npz.

*FIND IN CODE   Functions/CameraCalibration.py: def run_chessboard_calibration(srcImgPath, NumRows, NumColumns) [43-83]*

Distortion correction of an image is done by taking a distorted image, computing a new optimal camera matrix with distortion coefficients, and then undistorting the image with original camera matrix, distortion coefficients and new camera matrix. 

*FIND IN CODE   Functions/CameraCalibration.py: def distortion_correction(originalImg, srcImgName = None) [5-40]*

The camera calibration and image distortion correction can be tested with the given code:   > python calibration_main.py 

*FIND IN CODE   calibration_main.py: main [4-21]*

![plot](./output/sbys_calibration4.jpg)

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

TODO: Add your text here!!!

#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

TODO: Add your text here!!!

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

TODO: Add your text here!!!

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

TODO: Add your text here!!!

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

TODO: Add your text here!!!

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

TODO: Add your text here!!!

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

TODO: Add your text here!!!

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

TODO: Add your text here!!!

