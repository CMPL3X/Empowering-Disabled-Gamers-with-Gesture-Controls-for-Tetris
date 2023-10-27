# This code is used to make an video camera live stream that shows only the face to train the model
# Before running the script, you need to install the necessary packages. You can install OpenCV with pip install opencv-python and pip install pyvirtualcam opencv-python
# Also you have to have OBS installed and setup the obsvirtualcam

import cv2
import numpy as np
import pyvirtualcam

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

with pyvirtualcam.Camera(width=640, height=480, fps=30) as cam:
    while True:
        # Capture a frame from the webcam
        cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or change to the appropriate camera index
        ret, frame = cap.read()
        
        if not ret:
            continue

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # If faces are detected, process and send the frame to the virtual camera
        if len(faces) > 0:
            x, y, w, h = faces[0]
            face = frame[y:y+h, x:x+w]

            # Convert the processed frame to grayscale
            gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Convert the grayscale image back to BGR format
            gray_face_bgr = cv2.cvtColor(gray_face, cv2.COLOR_GRAY2BGR)

            # Resize the processed frame to match the virtual camera dimensions
            resized_face = cv2.resize(gray_face_bgr, (cam.width, cam.height))

            # Send the frame to the virtual camera
            cam.send(resized_face)

        # Release the webcam capture
        cap.release()
