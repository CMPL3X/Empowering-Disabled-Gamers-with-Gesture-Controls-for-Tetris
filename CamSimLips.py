import cv2
import numpy as np
import pyvirtualcam

# !!! REPLACE this paths with the absolute paths to the model
lip_cascade = cv2.CascadeClassifier('C:\\Users\\54132\\OneDrive\\Dators\\CoralTest\\Git\\Empowering-Disabled-Gamers-with-Gesture-Controls-for-Tetris\\haarcascade_mcs_mouth.xml')

with pyvirtualcam.Camera(width=640, height=480, fps=30) as cam:
    while True:
        # Capture a frame from the webcam
        cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or change to the appropriate camera index
        ret, frame = cap.read()
        
        if not ret:
            continue

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect lips in the grayscale frame
        lips = lip_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # If lips are detected, process and send the frame to the virtual camera
        if len(lips) > 0:
            for (x, y, w, h) in lips:
                lip = frame[y:y+h, x:x+w]

                # Convert the processed frame to grayscale
                gray_lip = cv2.cvtColor(lip, cv2.COLOR_BGR2GRAY)

                # Convert the grayscale image back to BGR format
                gray_lip_bgr = cv2.cvtColor(gray_lip, cv2.COLOR_GRAY2BGR)

                # Resize the processed frame to match the virtual camera dimensions
                resized_lip = cv2.resize(gray_lip_bgr, (cam.width, cam.height))

                # Send the frame to the virtual camera
                cam.send(resized_lip)

        # Release the webcam capture
        cap.release()
