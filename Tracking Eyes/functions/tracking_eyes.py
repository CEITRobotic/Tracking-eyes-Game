# Not finished still in progress

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def _detectEyes(img, cascade, gray_frame, f_rows, f_cols, contours):
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5)
    width = np.size(img, 1) 
    height = np.size(img, 0) 
    left_eye = None
    right_eye = None

    for (x,y,w,h) in eyes:
        if y + 50 < height / 2:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,100,0),2)
            for cnt in contours:
                (cx, cy, cw, ch) = cv2.boundingRect(cnt)
                if cy + 50 < ch / 2:
                    # cv2.drawContours(img, [cnt], -1, (0, 0, 255), 3)
                    cv2.rectangle(img, (cx, cy), (cx + cw, cy + ch), (0, 255, 0), 2)
                    cv2.line(img, (cx + int(cw/2), 0), (cx + int(cw/2), f_rows), (255, 0, 0), 1)
                    cv2.line(img, (0, cy + int(ch/2)), (f_cols, (cy + int(ch/2))), (255, 0, 0), 1)
            pass

        eyecenter = x + w / 2  # get the eye center

        if eyecenter < width * 0.5:
            left_eye = img[y:y + h, x:x + w]
        else:
            right_eye = img[y:y + h, x:x + w]
    return left_eye, right_eye


def openTracking():
    cap = cv2.VideoCapture(0)
    value = 42

    while(cap.isOpened()):
        _, frame = cap.read()
        # frame = frame[269:795, 537:1416]
        frame = cv2.flip(frame, 1)
        f_rows, f_cols, _ = frame.shape

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (7, 7), 0)

        _, threshold = cv2.threshold(gray_frame, value, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
            cv2.line(frame, (x + int(w / 2), 0), (x + int(w / 2), f_rows), (255, 255, 0), 1)

            # gray_face = gray_image[y:y+h, x:x+w]
            # face = frame[y:y+h, x:x+w]
            # eyes = eye_cascade.detectMultiScale(gray_face, 1.3, 5)

            _detectEyes(frame, eye_cascade, gray_frame, f_rows, f_cols, contours) 

            # for (ex,ey,ew,eh) in eyes: 
            #     cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,225,255),2)

        cv2.imshow('Camera', frame)
        cv2.imshow('Threshold', threshold)

        key = cv2.waitKey(1)
        if key == ord('i') and value < 255:
            value = value + 1
            print(value)
        elif key == ord('o') and value > 0:
            value = value - 1
            print(value)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
