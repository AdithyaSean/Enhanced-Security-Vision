import os
import cv2
from enhance import enhance_image

def detect_faces(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]

            # Path for saving the enhanced face image
            face_image_path = os.path.splitext(image_path)[0].replace('original', 'segmented') + '_face.jpg'
            cv2.imwrite(face_image_path, face)

            # Enhance the cropped face image and save it
            enhanced_face_path = face_image_path.replace('_face.jpg', '_enhanced_face.jpg')
            enhance_image(face_image_path, enhanced_face_path)

        print("Faces detected and enhanced successfully!")
    else:
        print("No faces detected.")