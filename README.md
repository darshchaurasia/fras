# Face Recognition Attendance System

A facial recognition-based attendance system using Python, OpenCV, and PostgreSQL.

## How to Use

1. **Install dependencies:**
   pip install -r requirements.txt

2. **Register a student:**
   Run register_student.py to capture the student's facial encoding and save it along with their name to the PostgreSQL database.

3. **Mark attendance:**
   Use video_capture.py to recognize faces and mark attendance. A confirmation message will be printed in the terminal.
   Note: Attendance is currently restricted to once per day per student. This limit can be adjusted with a single line of code change.

## Tech Stack

**Programming Language:**
- Python

**Libraries:**
- cv2 (OpenCV) – for image and video processing
- face_recognition – for facial encoding and recognition
- time – for handling timestamps and delays
- psycopg2 or similar (via postgres) – for connecting to the PostgreSQL database

**Database:**
- PostgreSQL

**Computer Vision:**
- Haar Cascades (for face detection)

**Scripts:**
- register_student.py – for capturing and storing facial data
- video_capture.py – for recognizing faces and marking attendance


## Author

Darsh Chaurasia (https://github.com/darshchaurasia)
