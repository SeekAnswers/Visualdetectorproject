import cv2
import numpy as np
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound(r"E:\Users\CHARLES\Documents\Ableton\User Library\sample packs\LoFi & Chill Collab Pack\Good Morning [88 BPM] G#.wav")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

is_drinking = False

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        mouth_roi = gray[y+h//2:y+h, x:x+w]
        _, mouth_thresh = cv2.threshold(mouth_roi, 50, 255, cv2.THRESH_BINARY)
        white_pixels = np.sum(mouth_thresh ==255)

        if white_pixels > 10000:
            if not is_drinking:
                print('Drinking coffee is detected!')
                is_drinking = True
                sound.play()
        else:
            is_drinking = False

        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('frame', frame)



# Check if the webcam is properly connected and accessible.
# Ensure no other application is using the webcam.
# If multiple video devices are present, try changing the index in cv2.VideoCapture(0) to the correct one.
# Use another application to test if the webcam is working outside of your script.
# Add error checking after cap.read() to handle cases where a frame is not captured.
#(while True:
#    ret, frame = cap.read()
#    if not ret:
#        print("Failed to grab frame")
#        continue)  # Skip the rest of the code in this iteration

    # ... rest of your code ...

# Include a condition to break out of the while loop, such as a key press.
# (   if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#
# Release the video capture and destroy all OpenCV windows after breaking out of the loop.
#(cap.release()
#cv2.destroyAllWindows()    )

# Handle potential errors, such as checking if the video capture is successful before processing the frame.
# Adjust the threshold for white_pixels based on the resolution of the video and the size of the mouth region.
# Verify that the .ogg file format is supported by Pygame and that the sound file is not corrupted.
# Tune the parameters in detectMultiScale based on the quality of the webcam and desired sensitivity.
