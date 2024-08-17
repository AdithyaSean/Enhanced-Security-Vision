import os
import cv2
from enhance import enhance_image
from night_vision import apply_night_vision

def detect_faces(image_path, intensity):
    upscale_factor = 2
    intensity_threshold = 50
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if intensity < intensity_threshold:
        image = apply_night_vision(gray)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]

            upscaled_face = cv2.resize(face, (w * upscale_factor, h * upscale_factor), interpolation=cv2.INTER_LINEAR)

            # Path for saving the enhanced face image
            face_image_path = os.path.splitext(image_path)[0].replace('original', 'segmented') + '_face.jpg'
            cv2.imwrite(face_image_path, upscaled_face)

            # Enhance the cropped face image and save it
            enhanced_face_path = face_image_path.replace('_face.jpg', '_enhanced_face.jpg')
            enhance_image(face_image_path, enhanced_face_path)

        print("Faces detected and enhanced successfully!")
    else:
        print("No faces detected.")