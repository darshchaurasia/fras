import cv2
from face_detector import detect_faces

def capture_video():
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)  # '0' is typically the default value for the first webcam

    if not cap.isOpened():
        print("Error: Camera is not accessible")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = detect_faces(gray)  # Directly pass the grayscale frame

            # Draw rectangles around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Press 'q' on the keyboard to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video()
