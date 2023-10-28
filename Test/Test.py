# This code is used to test, if the model is working corectly.
# Just put both (the .h5 and .txt files in the same folder!)
# pip install teachable-machine
# pip install opencv-python
 
from teachable_machine import TeachableMachine
import cv2
import numpy as np
import io
from PIL import Image

camera_port = 2 # !!! REPLACE this with your accual camera port. You can check with the cameraPortTest.py code

# !!! REPLACE these paths with the absolute paths to your model and labels files
model_path = "C:\\Users\\54132\\OneDrive\\Dators\\CoralTest\\Git\\Empowering-Disabled-Gamers-with-Gesture-Controls-for-Tetris\\Test\\keras_model.h5"
labels_path = "C:\\Users\\54132\\OneDrive\\Dators\\CoralTest\\Git\\Empowering-Disabled-Gamers-with-Gesture-Controls-for-Tetris\\Test\\labels.txt"

model = TeachableMachine(model_path=model_path, labels_file_path=labels_path)

# Open the camera stream
cap = cv2.VideoCapture(camera_port)

while True:
    _, img = cap.read()

    # Convert the image (numpy array) to bytes
    img_bytes = cv2.imencode('.jpg', img)[1].tobytes()
    
    # Classify the image
    result = model.classify_image(io.BytesIO(img_bytes))

    # Extract classification results
    class_index = result["class_index"]
    class_name = result["class_name"]
    class_confidence = result["class_confidence"]
    predictions = result["predictions"]

    # Print prediction and confidence score
    print("Class Index:", class_index)
    print("Class Confidence:", class_confidence)
    print("Predictions:", predictions)

    # Show the image in a window
    cv2.imshow("Webcam Image", img)

    if class_index == 0:
        print("Detected class 0")
    if class_index == 1:
        print("Detected class 1")
    if class_index == 2:
        print("Detected class 2")
    if class_index == 3:
        print("Detected class 3")

    # Listen to the keyboard for presses
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the Esc key on your keyboard
    if keyboard_input == 27:
        break

cap.release()
cv2.destroyAllWindows()