import cv2

def apply_night_vision(image):
    # Apply CLAHE for better contrast in dark areas
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(image)
    
    return enhanced_image