import numpy as np
import cv2

print("=== SONU-X SOFTWARE TEST ===")
print("Python + NumPy + OpenCV")

print("NumPy version:", np.__version__)
print("OpenCV version:", cv2.__version__)

image = np.zeros((300, 400, 3), dtype=np.uint8)

cv2.putText(
    image,
    "SONU-X TEST PASS",
    (70, 160),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imwrite("sonu_test.jpg", image)

print("Test image created: sonu_test.jpg")
print("SONU-X SOFTWARE TEST PASSED")