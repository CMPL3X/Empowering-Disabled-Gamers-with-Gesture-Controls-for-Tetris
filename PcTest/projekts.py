import tensorflowjs as tfjs
import numpy as np
import time
import cv2

model = tfjs.converters.load_keras_model('C:\\Users\\54132\\OneDrive\\Dators\\Test\\tm-my-image-model\\model.json')

cap = cv2.VideoCapture(1) #Change the camera port

while True:

    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0
    frame = np.expand_dims(frame, axis=0)
    
    frame = frame.astype(np.float32) # Convert image depth to float32

    prediction = model.predict(frame)

    print(prediction)

    if prediction[0][0] > prediction[0][1]:
        print("Happy")
    else:
        print("Sad")

    cv2.imshow('frame', cv2.cvtColor(frame[0].astype(np.uint8), cv2.COLOR_RGB2BGR)) # Convert image depth back to uint8

    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
