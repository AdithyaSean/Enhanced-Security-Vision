import os
import cv2

def detect_faces(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]
            enhanced_face_path = os.path.splitext(image_path)[0] + '_enhanced_face.jpg'
            cv2.imwrite(enhanced_face_path, face)
        print("Faces detected and segmented successfully!")
    else:
        print("No faces detected.")