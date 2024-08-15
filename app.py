import cv2

def calculate_average_intensity(frame):
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate the average intensity of the grayscale frame
    average_intensity = cv2.mean(gray_frame)[0]
    
    return average_intensity

def main():
    # Create a VideoCapture object to capture frames from the webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Calculate the average intensity of the frame
        average_intensity = calculate_average_intensity(frame)
        
        # Display the average intensity on the frame
        cv2.putText(frame, f"Average Intensity: {average_intensity:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Show the frame
        cv2.imshow("Webcam", frame)
        
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the VideoCapture object and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()