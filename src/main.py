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
    cv2.imshow("webcam", frame)

    elapsed_time_sec = (datetime.now() - start_time_sec).total_seconds()

    intensity = np.mean(cv2.split(frame))
    print("Intensity:", int(intensity))

    if elapsed_time_sec >= 5:
        if previous_intensity is not None and np.any(cv2.absdiff(intensity, previous_intensity)) > 2:
            print("Change in intensity detected!")
            change_detected = True
            frame_counter += 1
            timestamp = datetime.now().strftime("M%S")
            print(f"Saving frames...")
            frame_path_original = f"./original/frame_{timestamp}_{frame_counter}.jpg"
            frame_path_segmented = f"./segmented/frame_{timestamp}_{frame_counter}.jpg"
            cv2.imwrite(frame_path_original, frame)
            cv2.imwrite(frame_path_segmented, detect_faces(frame_path_original))
        previous_intensity = intensity
        start_time_sec = datetime.now()

    if elapsed_time_sec >= 10:
        if not change_detected:
            print("No considerable intensity change detected.")
        change_detected = False
        start_time_10_sec = datetime.now()

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()