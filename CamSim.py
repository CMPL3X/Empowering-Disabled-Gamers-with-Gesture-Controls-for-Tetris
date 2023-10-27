# Used to output a clean webcam image for the AI

import cv2
import obspython as obs

# Initialize the OBS API
obs.obs_frontend_get_current_scene()
context = obs.obs_frontend_get_main_output()
obs_output = obs.obs_frontend_get_output_by_name("VirtualCam")

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or change to the appropriate camera index

# Set the desired brightness level
desired_brightness = 1.5  # Adjust this value to control the brightness (1.0 is no change)

# Function to process each frame
def filter_frame(filter, settings, source, data):
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        return

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If faces are detected, zoom into the first detected face and adjust brightness
    if len(faces) > 0:
        x, y, w, h = faces[0]
        face = frame[y:y+h, x:x+w]

        # Adjust brightness
        face = cv2.convertScaleAbs(face, alpha=desired_brightness, beta=0)

        # Convert the processed frame to RGBA format for OBS
        frame_rgba = cv2.cvtColor(face, cv2.COLOR_BGR2BGRA)

        # Send the frame to OBS
        obs.obs_source_process_video(filter, frame_rgba, None, None)

# Register the filter
obs.obs_register_source_filter("FaceFilter", "Face Filter", filter_frame)

# Initialize the virtual camera
obs.obs_source_output_set_audio_output_id(obs_output, obs.OBS_INVALID_AUDIO_OUTPUT)

# Run OBS
obs.obs_frontend_replay_buffer_start()

# Main loop (run OBS)
obs.obs_frontend_run()

# Release resources when OBS is closed
obs.obs_source_output_set_audio_output_id(obs_output, obs.OBS_INVALID_AUDIO_OUTPUT)
obs.obs_frontend_replay_buffer_stop()
cap.release()
cv2.destroyAllWindows()
