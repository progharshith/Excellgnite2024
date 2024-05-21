from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np
import pyautogui

# Create a camera window
camera_window = np.zeros((800, 800, 3), dtype=np.uint8)
camera_window[:] = (29, 9, 26)  # Set the background color to purple

# Initialize Hand Detector
detector = HandDetector(detectionCon=0.8)

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize variables to track the finger states
prev_index_finger_up = False
prev_thumb_up = False

while True:
    # Get image frame
    success, img = cap.read()

    if not success:
        print("Failed to read frame from the camera.")
        break

    img = cv2.flip(img, 1)

    # Find the hand and its landmarks
    hands, _ = detector.findHands(img)  # with draw

    # Check if only index finger or thumb is raised
    index_finger_up = False
    thumb_up = False
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
       
        # Only index finger is raised
        index_finger_up = fingers[1] == 1 and all(f == 0 for i, f in enumerate(fingers) if i != 1)
       
        # Only thumb is raised
        thumb_up = fingers[0] == 1 and all(f == 0 for i, f in enumerate(fingers) if i != 0)

    # If only index finger is raised and it wasn't raised in the previous frame, move forward in the slides
    if index_finger_up and not prev_index_finger_up:
        pyautogui.press('right')
        print("Moved forward in the slides")

    # If only thumb is raised and it wasn't raised in the previous frame, move backward in the slides
    if thumb_up and not prev_thumb_up:
        pyautogui.press('left')
        print("Moved backward in the slides")

    # Update the previous states
    prev_index_finger_up = index_finger_up
    prev_thumb_up = thumb_up

    # Display the live camera feed on the camera window
    camera_window[:, :] = cv2.resize(img, (800, 800))

    # Display the windows
    cv2.imshow("Camera Window", camera_window)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
