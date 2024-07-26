import requests
import cv2

# Define the API endpoint
api_endpoint = "http://your-api-endpoint.com/detect"

# Open the device's camera
camera = cv2.VideoCapture(0)

while True:
    # Read the current frame from the camera
    ret, frame = camera.read()

    # Convert the frame to base64
    _, img_encoded = cv2.imencode('.jpg', frame)
    base64_image = img_encoded.tobytes()

    # Send the image to the API for detection
    response = requests.post(api_endpoint, data=base64_image)

    # Process the response
    if response.status_code == 200:
        # Parse the response to get the detection results
        detection_results = response.json()

        # Process the detection results
        # ...

    # Display the frame with the detection results
    cv2.imshow("Camera", frame)

    # Check for key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()