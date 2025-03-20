import cv2
import mediapipe as mp
import numpy as np
import pygame

# Initialize pygame for sound
pygame.mixer.init()

# Load piano sounds
piano_sounds = {
    "C4": pygame.mixer.Sound("sounds/C4.wav"),
    "D4": pygame.mixer.Sound("sounds/D4.wav"),
    "E4": pygame.mixer.Sound("sounds/E4.wav"),
    "F4": pygame.mixer.Sound("sounds/F4.wav"),
}

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror effect
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index finger tip position
            index_finger = hand_landmarks.landmark[8]  # Index finger tip
            x = index_finger.x  # Normalized (0-1)
            y = index_finger.y  # Normalized (0-1)

            # Map x-position to piano notes
            if x < 0.25:
                piano_sounds["C4"].play()
            elif 0.25 <= x < 0.50:
                piano_sounds["D4"].play()
            elif 0.50 <= x < 0.75:
                piano_sounds["E4"].play()
            else:
                piano_sounds["F4"].play()

    # Display webcam feed
    cv2.imshow("Virtual Piano", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
