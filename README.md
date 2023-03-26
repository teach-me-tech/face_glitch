Face Blur and Glitch Application

This is a Python-based application that can blur the faces in a video or a live video feed using OpenCV and also apply a glitch effect to the blurred region.

Dependencies
  1. Python 3
  2. OpenCV (cv2)
  3. Numpy
Installation
  1. Install Python 3 from the official website - https://www.python.org/downloads/

  2.Install OpenCV and Numpy using pip:

  3.pip install opencv-python numpy

  Download the haarcascade_frontalface_default.xml file which is used by OpenCV for face detection. It can be downloaded from the following link -      https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

Usage
  1. Clone the repository or download the source code.

  2. Save the haarcascade_frontalface_default.xml file in the same directory as the code file.

  3. Run the code using the following command:
      python face_blur_glitch.py

  5. A window will open showing the live feed from the camera. Press the ESC key to exit the application.

  To change the amount of blur or the intensity of the glitch effect, change the values of blur_amount and glitch_intensity respectively.

Acknowledgements
The code for the face detection using OpenCV was adapted from the OpenCV Face Detection Documentation
