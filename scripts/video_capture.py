import cv2
from face_detector import detect_and_encode_faces

def capture_video():
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

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

            # Detect and encode faces
            encodings = detect_and_encode_faces(frame)

            # Draw rectangles around the faces and display encoding length (as a proxy for seeing something happened)
            for encoding, (x, y, w, h) in encodings:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, f"Encoded: {len(encoding)}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

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
