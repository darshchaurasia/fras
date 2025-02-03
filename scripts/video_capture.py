import cv2
import numpy as np
from face_detector import detect_and_encode_faces
from database import log_attendance, get_student_encodings, has_attendance_been_logged_today

def recognize_and_log_faces(frame):
    face_data = detect_and_encode_faces(frame)
    known_faces = get_student_encodings()  # Fetch known faces each time to ensure up-to-date information

    for encoding, (top, right, bottom, left) in face_data:
        x, y, w, h = left, top, right - left, bottom - top
        match_found = False

        for student_id, known_encoding in known_faces.items():
            distance = np.linalg.norm(encoding - known_encoding)
            if distance < 0.6:
                if not has_attendance_been_logged_today(student_id):  # Check if attendance has already been logged today
                    log_attendance(student_id)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green rectangle for recognized and logged
                    cv2.putText(frame, "Attendance Recorded", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    match_found = True
                    break

        if not match_found:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)  # Red rectangle for unrecognized

def capture_video():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera is not accessible")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            recognize_and_log_faces(frame)

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video()
