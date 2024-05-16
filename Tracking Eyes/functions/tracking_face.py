import cv2
from . import control_cursor as cc

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def openTracking():
    cap = cv2.VideoCapture(0)
    cx = 0 
    cy = 0
    
    while(cap.isOpened()):
        title = 'Open Tracking...'

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

        f_rows, f_cols, _ = frame.shape

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (7, 7), 0)

        faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

        for (x, y, w, h) in faces:
            cy = (y + int(h/2))
            cx = (x + int(w/2))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv2.circle(frame, (x + int(w/2), y + int(h/2)), 5, (0, 155, 255), 1)
            cv2.line(frame, (x + int(w/2), 0), (x + int(w/2), f_rows), (255, 255, 0), 1)
            cv2.line(frame, (0, y + int(h/2)), (f_cols, y + int(h/2)), (255, 255, 0), 1)
            cv2.line(frame, (x + int(w/2), y + int(h/2)), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/2)), (0, 255, 0), 1)

            cv2.putText(frame, title, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Display the x and y axis coordinates near the face
            cv2.putText(frame, f"X: {cx}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(frame, f"Y: {cy}", (x + w, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Update cursor position based on face tracking
        cc.controlCursor(cx, cy, int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/2))

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) == ord('q'):
            print("\nExiting...")
            break
 
    cap.release()
    cv2.destroyAllWindows()
