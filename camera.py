from datetime import datetime
import os
import cv2
import logging

logger = logging.getLogger(__name__)

OUTPUT_FOLDER = "captured_images"

# Create the output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def take_picture():
    # Initialize the webcam
    camera = cv2.VideoCapture('http://localhost:5000/video_feed')
    destination_file_path = None

    if not camera.isOpened():
        msg = "Error: Could not open webcam."
        print(msg)
        logger.error(msg)
        return

    # Show the webcam feed
    print("Press 's' to save the picture, or 'q' to quit without saving.")
    while True:
        # Capture a frame
        successful, frame = camera.read()
        
        if not successful:
            msg = "Failed to grab frame."
            print(msg)
            logger.error(msg)
            break

        # Display the frame
        cv2.imshow("Webcam", frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Press 's' to save the picture
            destination_file_path = os.path.join(OUTPUT_FOLDER, str(datetime.now()) + ".jpg")
            cv2.imwrite(destination_file_path, frame)
            logger.info("Picture saved as: " + destination_file_path)
            break
        elif key == ord('q'):  # Press 'q' to quit without saving
            logger.info("Exiting without saving.")
            break

    # Release the camera and close the window
    camera.release()
    cv2.destroyAllWindows()
    return destination_file_path
