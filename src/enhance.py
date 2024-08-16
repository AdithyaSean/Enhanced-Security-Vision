import cv2
import numpy as np
import os

def enhance_image(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print(f"Failed to load image from {image_path}")
        return None

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to improve contrast
    equalized = cv2.equalizeHist(gray)

    # Convert back to BGR for sharpening
    equalized_bgr = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    
    # Apply sharpening using the kernel
    sharpened = cv2.filter2D(equalized_bgr, -1, kernel)

    # Save the enhanced image to the specified output path
    enhanced_face_image_path = os.path.splitext(image_path)[0].replace('segmented', 'enhanced') + '_face.jpg'
    cv2.imwrite(enhanced_face_image_path, sharpened)

    print(f"Enhanced image saved to {output_path}")
    return output_path