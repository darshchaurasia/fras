import cv2
import face_recognition

def detect_and_encode_faces(frame):
    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
    
    # Convert frame to gray scale if it's not already
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if len(frame.shape) == 3 else frame

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # List for storing face encodings
    encodings = []

    for (x, y, w, h) in faces:
        # Extract each face
        face_frame = frame[y:y+h, x:x+w]

        # Convert the face from BGR to RGB (face_recognition uses RGB)
        rgb_face = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)

        # Encode the face
        current_encoding = face_recognition.face_encodings(rgb_face)

        if current_encoding:
            encodings.append((current_encoding[0], (x, y, w, h)))

    return encodings  # Return the encodings and the corresponding face locations
