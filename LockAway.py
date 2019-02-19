# Hayden Riewe
# github.com/hriewe
# hrcyber.tech

import numpy as np
import cv2
import subprocess
import sys

# Set up variables
cap = cv2.VideoCapture(0)
lockCounter = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert fram to black and white image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle on face, not necessary
    for (x,y,w,h) in faces:   
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w] 

    # Determine if face in in view, if not lock Mac
    if len(faces) > 0:
        lockCounter = 0
    else:
        lockCounter = lockCounter + 1

    # This variable determines how many frames pass without a face before Mac locks
    if lockCounter >= 10:
        subprocess.call('/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend',
            shell=True)
        sys.exit()

    # Display the resulting frame, used for testing
    cv2.imshow('LockAway', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()