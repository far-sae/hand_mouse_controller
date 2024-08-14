import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(0)

# Get the screen size
screen_width, screen_height = pyautogui.size()

def calculate_distance(point1, point2, width, height):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) * min(width, height)

while True:
    # Capture frame from the webcam
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)

    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and detect hand landmarks
    results = hands.process(image_rgb)

    # Get the dimensions of the image
    image_height, image_width, _ = image.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the tip of the index finger (landmark 8) and the tip of the thumb (landmark 4)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Convert the normalized coordinates to screen coordinates
            finger_x = int(index_finger_tip.x * screen_width)
            finger_y = int(index_finger_tip.y * screen_height)

            # Move the mouse to the index finger position
            pyautogui.moveTo(finger_x, finger_y)

            # Calculate the distance between the thumb and index finger
            distance = calculate_distance(index_finger_tip, thumb_tip, image_width, image_height)

            # If the distance is below a threshold, perform a click
            if distance < 30:  # Adjust the threshold as necessary
                pyautogui.click()

    # Display the image with hand landmarks
    cv2.imshow('Hand Tracking', image)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
