# excellgnite2024
The projects/codes made by us at an internship at Excelsoft Technologies.

# 1. The Slide Changer
 *(Hand Gesture Controlled Slide Navigation)*

This project demonstrates a hand gesture-controlled slide navigation system using a webcam. The system leverages computer vision techniques to detect hand gestures and uses these gestures to navigate through slides. The code is written in Python and utilizes several libraries to achieve this functionality.

## Features

- The camera feed is displayed in a custom window with a cyberpunk theme.
- Hand gesture detection: Detects when the index finger or thumb is raised.
- Slide navigation: Uses hand gestures to move forward or backward in the slides.

## Requirements

- Python
- OpenCV
- NumPy
- PyAutoGUI
- CVZone (HandTrackingModule)

## *Code Overview*
## 1.Camera Initialization
> A webcam feed is captured using OpenCV.
> The feed is displayed in a custom window with a cyberpunk-themed background.
## 2.Hand Detection
> The HandDetector class from the cvzone library is used to detect hand landmarks.
> The script checks which fingers are raised using the fingersUp method.
## 3.Gesture Recognition
> If only the index finger is raised, the script simulates a "right arrow" key press to move forward in the slides.
> If only the thumb is raised, the script simulates a "left arrow" key press to move backward in the slides.
## 4. Loop and Exit
> The script runs in a loop, continuously processing the webcam feed.
> Press 'q' to exit the program.

*Note: This code runs in python and requires you to have the prerequisites mentioned, aswell as have the powerpoint file open as this code simply uses "left" and "right" of pyautogui*

Feel free to fork! Happy coding!

For any questions or suggestions, Contact us!
[harshithguptaa2@gmail.com],[harshul.the.kaushal@gmail.com]
