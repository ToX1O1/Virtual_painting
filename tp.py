# import cv2
# import numpy as np

# # Function to detect thumb position and button area in real-time
# def detect_thumb_and_button():
#     # Load pre-trained hand detection model
#     hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_hand.xml')

#     # Open video capture device
#     cap = cv2.VideoCapture(0)

#     while True:
#         # Read a frame from the video capture
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Convert frame to grayscale for hand detection
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect hands in the frame
#         hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

#         # Draw rectangles around detected hands
#         for (x, y, w, h) in hands:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#             # Extract thumb position (center of the hand)
#             thumb_position = (x + w // 2, y + h // 2)

#             # Define button area (example values)
#             button_x = x + w // 2 - 25
#             button_y = y + h // 2 + 50
#             button_w = 50
#             button_h = 50
#             button_area = (button_x, button_y, button_w, button_h)

#             # Check if button is pressed
#             is_button_pressed = button_pressed(thumb_position, button_area)

#             # Draw button area rectangle
#             cv2.rectangle(frame, (button_x, button_y), (button_x + button_w, button_y + button_h), (0, 255, 0), 2)

#             # Display button press status
#             if is_button_pressed:
#                 cv2.putText(frame, 'Button Pressed', (button_x, button_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#             else:
#                 cv2.putText(frame, 'Button Not Pressed', (button_x, button_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

#         # Display the frame
#         cv2.imshow('Thumb and Button Detection', frame)

#         # Exit if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture device and close all OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()

# # Function to simulate button press event based on thumb position and button area
# def button_pressed(thumb_position, button_area):
#     thumb_x, thumb_y = thumb_position
#     button_x, button_y, button_w, button_h = button_area

#     # Check if thumb position is within button area
#     if button_x < thumb_x < button_x + button_w and button_y < thumb_y < button_y + button_h:
#         return True
#     else:
#         return False

# # Run thumb and button detection function
# detect_thumb_and_button()
