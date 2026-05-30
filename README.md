Face Detection using OpenCV

This is a simple Python project that detects human faces using OpenCV and Haar Cascade classifier.

Features:
- Detects faces in real-time using webcam
- Draws rectangle around detected faces

Requirements:
- Python 3
- OpenCV


How to run:
1. Open terminal
2. Go to project folder
   cd your-folder-name
3. Run the program
   python3 face_detection.py

Controls:
- Press 'q' to quit the webcam window

How it works:
- Webcam captures video
- Converts frames to grayscale
- Detects faces using Haar Cascade
- Draws rectangle around faces

Output:
- Webcam window opens with face detection boxes

Note:
- Uses Haar Cascade (haarcascade_frontalface.xml)
- Works best in good lighting conditions
