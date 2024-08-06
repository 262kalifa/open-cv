import cv2

# Open a connection to the webcam (use 0 for the default webcam, or 1, 2, etc. for other cameras)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define the codec and create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Create VideoWriter object

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured correctly
    if not ret:
        print("Error: Could not read frame.")
        break

    # Write the frame to the output video file
    out.write(frame)

    # Display the frame in a window
    cv2.imshow('Webcam Video', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and video writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
