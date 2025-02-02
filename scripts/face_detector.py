import cv2

def detect_faces(frame):
    # Assuming frame is already in grayscale if not convert it here
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if len(frame.shape) == 3 else frame

    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    return faces  # Coordinates of detected faces
