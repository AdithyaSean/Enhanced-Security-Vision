import os
import cv2
from datetime import datetime
import numpy as np
from segment import detect_faces

# Directory names
directories_to_create = ["original", "segmented", "enhanced"]

# Create directories if they don't exist
for directory in directories_to_create:
    os.makedirs(directory, exist_ok=True)

# Replace the webcam URL with the ESP32-CAM video stream URL
esp32_cam_url = "http://192.168.1.18:81/stream"

# Open the video stream from the ESP32-CAM
cap = cv2.VideoCapture(esp32_cam_url)

# Check if the video stream is opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream from ESP32-CAM.")
    exit()

start_time_sec = datetime.now()
previous_intensity = None
change_detected = False
frame_counter = 0

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame from ESP32-CAM")
            break

        elapsed_time_sec = (datetime.now() - start_time_sec).total_seconds()

        intensity = np.mean(frame)
        print("Intensity:", int(intensity))

        if previous_intensity is not None and abs(intensity - previous_intensity) >= 2:
            print("Change in intensity detected!")
            change_detected = True
            frame_counter += 1
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            frame_path_original = f"original/frame_{timestamp}_{frame_counter}.jpg"
            cv2.imwrite(frame_path_original, frame)
            detect_faces(frame_path_original, intensity)

        previous_intensity = intensity

except KeyboardInterrupt:
    print("Program interrupted by user. Exiting...")

finally:
    # Release the video capture object
    cap.release()
    print("Video stream released.")
