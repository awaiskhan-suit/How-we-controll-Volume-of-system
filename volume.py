import cv2
import mediapipe as mp
import math
# control Windows sound
# pycaw.pycaw → internal module where audio classes exist
# AudioUtilities access audio devices (speakers, headphones, mic)
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER

# -------------------- Setup Pycaw (latest method) --------------------
devices = AudioUtilities.GetSpeakers() # default spekar
volume = devices.EndpointVolume  # increase or decrease volume

# -------------------- Setup MediaPipe Hands ----------------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# -------------------- Open Webcam ----------------------------
cap = cv2.VideoCapture(0)

# (x1, y1) → Index finger tip position
# (x2, y2) → Thumb tip position

x1 = y1 = x2 = y2 = 0

# Distance to volume mapping thresholds
MIN_DISTANCE = 30    # fingers very close → volume 0%
MAX_DISTANCE = 150   # fingers far apart → volume 100%

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            for id, lm in enumerate(hand_landmarks.landmark): # enumerate give both index and volume
                x = int(lm.x * frame_w)
                y = int(lm.y * frame_h)

                if id == 8:  # Index finger tip
                    x1, y1 = x, y
                    cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

                if id == 4:  # Thumb tip
                    x2, y2 = x, y
                    cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

            # Draw line between thumb & index finger
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # Calculate distance
            distance = math.hypot(x2 - x1, y2 - y1)
            cv2.putText(frame, f"Distance: {int(distance)}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # ---------------- Gesture Based Volume ----------------
            # Clamp distance within thresholds
            # Do not allow a value to go below a minimum
            # Do not allow it to go above a maximum
            distance_clamped = max(MIN_DISTANCE, min(distance, MAX_DISTANCE))

            # Map distance to volume (0.0 - 1.0)
            vol = (distance_clamped - MIN_DISTANCE) / (MAX_DISTANCE - MIN_DISTANCE)

            # Set system volume
            volume.SetMasterVolumeLevelScalar(vol, None)

            # Display volume percentage
            cv2.putText(frame, f"Volume: {int(vol*100)}%", (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show frame
    cv2.imshow("Hand Gesture Volume Control", frame)

    # Press 'p' to exit
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

cap.release()
cv2.destroyAllWindows()

