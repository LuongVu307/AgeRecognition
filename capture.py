import cv2 
import os



def capture(file_path='example.jpg', camera_index=0):
    MAIN_PATH = os.getcwd()
    # Open a connection to the webcam (camera_index is usually 0 for the default camera)
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Couldn't open camera.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Couldn't capture frame.")
        cap.release()
        return

    # Save the captured frame to a file
    cv2.imwrite(os.path.join(MAIN_PATH, file_path), frame)

    # Release the camera
    cap.release()

    print(f"Image captured and saved to {file_path}")



capture()