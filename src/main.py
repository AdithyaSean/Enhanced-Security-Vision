import cv2
from datetime import datetime
import numpy as np
from segment import detect_faces

cap = cv2.VideoCapture(0)
start_time_sec = datetime.now()
previous_intensity = None
change_detected = False
frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("webcam", frame)

    elapsed_time_sec = (datetime.now() - start_time_sec).total_seconds()

    intensity = np.mean(frame)
    print("Intensity:", int(intensity))

    if previous_intensity is not None and abs(intensity - previous_intensity) >= 1:
        print("Change in intensity detected!")
        change_detected = True
        frame_counter += 1
        timestamp = datetime.now().strftime("%M%S")
        frame_path_original = f"original/frame_{timestamp}_{frame_counter}.jpg"
        cv2.imwrite(frame_path_original, frame)
        detect_faces(frame_path_original, intensity)

    previous_intensity = intensity

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()