
import cv2

camera = cv2.VideoCapture(0)
# 0 = default webcam, 1 = external camera

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
# loads pre-trained face detection model (XML file)

while True:
    ret, frame = camera.read()
    # reads one frame from webcam

    if not ret:
        print("camera not detected!")
        break
    # stops loop if camera is not working

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # converts color image to grayscale for better detection

    faces = face_cascade.detectMultiScale(gray)
    # detects faces in the image

    for (x, y, w, h) in faces:
        # x, y = top-left corner of face box
        # w, h = width and height of face box

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        # draws rectangle around detected face

    cv2.imshow("FaceDetected", frame)
    # shows the video with detection box

    key = cv2.waitKey(1)
    # waits 1 ms and checks for keyboard input

    if key & 0xFF == ord('q'):
        # press 'q' to quit the program
        print("Detection stopped")
        break

camera.release()
# releases webcam (turns off camera)

cv2.destroyAllWindows()
# closes all OpenCV windows