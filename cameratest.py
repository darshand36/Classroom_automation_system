# import cv2

# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# if ret:
#     cv2.imshow("Webcam Test", frame)
#     cv2.waitKey(0)
# else:
#     print("Cannot access the camera.")
# cap.release()
# cv2.destroyAllWindows()

import cv2

# Try connecting to different indices to find the Iriun camera
# for index in range(5):  # Adjust range if necessary
#     cap = cv2.VideoCapture(index)
#     if cap.isOpened():
#         print(f"Camera found at index {index}")
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow(f"Camera {index}", frame)
#             cv2.waitKey(2000)  # Show for 2 seconds
#         cap.release()
#         cv2.destroyAllWindows()
#     else:
#         print(f"No camera at index {index}")
cap = cv2.VideoCapture(2)  # Use the detected index for Iriun Webcam
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Iriun Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
