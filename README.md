Real-Time Pedestrian Detection with OpenCV

This Python program implements a real-time pedestrian detection system using OpenCV. It can process video streams from a webcam or pre-recorded videos to identify pedestrians.

Components:

Libraries:

OpenCV (cv2): Provides image and video processing functionalities.
NumPy (Optional): Used for efficient array manipulation during processing (common in deep learning models).
Model:

The system utilizes OpenCV's built-in pedestrian detection model based on Histogram of Oriented Gradients (HOG) features and a Support Vector Machine (SVM) classifier. HOG captures local gradients and edge information in the image, which are effective for pedestrian detection. The SVM has been trained to distinguish pedestrians from other objects in the scene.
Functionality:

Initialization:

Load the pre-trained HOG+SVM pedestrian detection model using OpenCV's cv2.HOGDescriptor_getDefaultPeopleDetector() function.
Initialize video capture using cv2.VideoCapture(), specifying either webcam index (0 for default) or a video file path.
Frame Processing Loop:

Capture each frame from the video stream using cap.read().
(Optional) Pre-process the frame: resize to a standard size or convert to grayscale for efficiency (depending on model requirements).
Use the loaded pedestrian detector to identify pedestrians in the frame with hog.detectMultiScale(frame). This function returns an array of bounding boxes (rectangles) around detected pedestrians and their confidence scores.
Iterate through the detected pedestrians:
Extract bounding box coordinates (x, y, width, height).
Draw a rectangle around the pedestrian on the original frame using OpenCV's drawing functions.
(Optional) Display the confidence score of the detection next to the bounding box.
Output:

Display the processed frame with bounding boxes using cv2.imshow().
Update the window and wait for a key press to exit (e.g., 'q' for quit).
