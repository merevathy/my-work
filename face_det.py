import cv2

def main():
    # Load the cascade
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print(f"Error: Could not load cascade classifier from {cascade_path}")
        return

    print("Face detection started. Press 'Esc' to exit.")

    # To capture video from webcam. 
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    print("Webcam opened successfully.")

    while True:
        # Read the frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the count of faces
        count_text = f"Faces: {len(faces)}"
        cv2.putText(frame, count_text, (frame.shape[1] - 150, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display
        cv2.imshow('Face Detection', frame)
        cv2.setWindowProperty('Face Detection', cv2.WND_PROP_TOPMOST, 1)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
