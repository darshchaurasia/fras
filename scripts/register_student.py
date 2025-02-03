import cv2
import face_recognition
from database import add_student

def capture_face_encoding():
    cap = cv2.VideoCapture(0)
    print("Adjust your position in front of the camera. Press 'c' to capture when ready.")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Display the video
        cv2.imshow('Video', frame)
        
        # Wait for the user to press 'c' to capture the face
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Convert the image from BGR color (which OpenCV uses) to RGB color
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            if face_encodings:
                print("Face captured successfully.")
                cap.release()
                cv2.destroyAllWindows()
                return face_encodings[0]

        # Allow the user to quit the registration by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Registration cancelled.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return None  # Return None if no faces are detected or registration is cancelled

def register_student():
    student_name = input("Enter the name of the student: ")
    print("Please look directly into the camera to capture face encoding.")
    face_encoding = capture_face_encoding()

    if face_encoding is not None:
        student_id = add_student(student_name, face_encoding)
        print(f"Student {student_name} registered successfully with ID {student_id}.")
    else:
        print("Failed to capture face encoding. Please try again.")

if __name__ == "__main__":
    register_student()
