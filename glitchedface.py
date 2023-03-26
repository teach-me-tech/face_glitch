import cv2
import urllib.request
import numpy as np

# # Download the face detection classifier
# url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
# urllib.request.urlretrieve(url, 'haarcascade_frontalface_default.xml')

# Load the face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create a video capture object to read frames from the camera
cap = cv2.VideoCapture(0)

# Loop through the frames in the video stream
while True:
    # Read the next frame from the camera
    ret, frame = cap.read()

    # Detect faces in the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Blur the detected faces
    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        face_glitch = cv2.stylization(face_roi, sigma_s=60, sigma_r=0.7)
        face_glitch_color = cv2.applyColorMap(face_glitch, cv2.COLORMAP_JET)
        # Combine original and glitched images with XOR operation
        height, width, channels = face_roi.shape
        rand_x = np.random.randint(-5, 5)
        rand_y = np.random.randint(-5, 5)
        mask = np.zeros((height, width), dtype=np.uint8)
        mask[rand_y:y+h+rand_y, rand_x:x+w+rand_x] = 255
        face_glitch_masked = cv2.bitwise_xor(face_roi, face_glitch_color, mask=mask)
        frame[y:y+h, x:x+w] = face_glitch_masked
        
    # Display the processed frame in a window
    cv2.imshow('Blurred Video', frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Check if the Esc key is pressed
    if cv2.waitKey(1) == 27:
        break

    # # Check if the window is closed
    # if cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
    #     break

# Release the resources
cap.release()
cv2.destroyAllWindows()
