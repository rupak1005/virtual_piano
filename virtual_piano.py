import cv2
import pygame
import numpy as np
import time

# Initialize Pygame mixer for sound playback
pygame.mixer.init()

# Load piano sounds (Mapping each finger to a specific note)
sound_files = {
    0: "sounds/a6-82015.mp3",
    1: "sounds/a6-102820.mp3",
    2: "sounds/b6-82017.mp3",
    3: "sounds/c6-102822.mp3",
    4: "sounds/d6-82018.mp3",
    5: "sounds/d6-82020.mp3",
    6: "sounds/e6-82016.mp3",
    7: "sounds/f6-102819.mp3",
    8: "sounds/g6-82013.mp3",
    9: "sounds/g6-82014.mp3"
}

# Convert to pygame sound objects
sounds = {finger: pygame.mixer.Sound(file) for finger, file in sound_files.items()}

# Open webcam
cap = cv2.VideoCapture(0)
last_played = {i: 0 for i in range(10)}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror effect
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define skin color range
    lower_skin = np.array([0, 30, 60], dtype=np.uint8)
    upper_skin = np.array([20, 150, 255], dtype=np.uint8)

    # Create mask
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        
        if cv2.contourArea(max_contour) > 2000:  # Adjust size threshold
            hull = cv2.convexHull(max_contour, returnPoints=False)
            defects = cv2.convexityDefects(max_contour, hull)

            if defects is not None:
                fingertips = []
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(max_contour[s][0])
                    end = tuple(max_contour[e][0])
                    far = tuple(max_contour[f][0])

                    # Use distance from hull to detect fingertips
                    if d > 10000:
                        fingertips.append(start)
                        fingertips.append(end)

                # Remove duplicates
                fingertips = list(set(fingertips))

                # Play sound based on number of detected fingers
                num_fingers = min(len(fingertips), 10)  # Limit to 10 sounds

                if num_fingers > 0 and time.time() - last_played[num_fingers] > 0.5:
                    sounds[num_fingers - 1].play()
                    last_played[num_fingers] = time.time()

                # Draw fingertips
                for fingertip in fingertips:
                    cv2.circle(frame, fingertip, 10, (0, 255, 0), -1)

    # Show webcam feed
    cv2.imshow("Virtual Piano", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
