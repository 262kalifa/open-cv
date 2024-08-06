import cv2

# Load an image from file
image = cv2.imread('path/to/your/image.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Display the image in a window
    cv2.imshow('Loaded Image', image)

    # Wait for a key press indefinitely or for a specified amount of time in milliseconds
    cv2.waitKey(0)  # 0 means wait indefinitely

    # Save the image to a new file
    cv2.imwrite('path/to/save/image.jpg', image)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
