import os
import cv2
import numpy as np
import tensorflow as tf

# Replace these with the actual paths to your model and label files
modelPath = 'model_edgetpu.tflite'
labelPath = 'labels.txt'

# Load labels
with open(labelPath, 'r') as f:
    labels = f.read().strip().split('\n')

def classifyImage(interpreter, image):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data

def main():
    interpreter = tf.lite.Interpreter(model_path=modelPath)
    interpreter.allocate_tensors()

    cap = cv2.VideoCapture(0)  # Use 0 for the default camera

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        resized_frame = cv2.resize(frame, (224, 224))  # Adjust the size to match your model's input size

        input_data = np.expand_dims(resized_frame, axis=0)
        input_data = (input_data.astype(np.float32) - 127.5) / 127.5  # Normalize if needed

        results = classifyImage(interpreter, input_data)
        label_id = np.argmax(results)
        confidence = results[0, label_id]

        label = labels[label_id]

        print(f"{label} - Confidence: {confidence:.2f}%")

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
