import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="numpy")

import tensorflowjs as tfjs
import numpy as np
import cv2

model = tfjs.converters.load_keras_model('C:\\Users\\54132\\OneDrive\\Dators\\CampIT2023\\Test\\tm-my-image-model\\model.json')

cap = cv2.VideoCapture(1)

Vards = input("Kā tevi sauc? : ")

while True:

    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0
    frame = np.expand_dims(frame, axis=0)

    prediction = model.predict(frame)

    if prediction[0][0] > prediction[0][1]:
        print(Vards + " ir priecīgs")
    else:
        print(Vards + " ir dusmīgs")

    frame = (frame * 255).astype(np.uint8)
    cv2.imshow('frame', cv2.cvtColor(frame[0], cv2.COLOR_RGB2BGR))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
