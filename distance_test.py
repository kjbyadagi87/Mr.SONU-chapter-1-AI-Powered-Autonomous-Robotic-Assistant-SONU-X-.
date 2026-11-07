import cv2

print("=== SONU-X OBSTACLE DISTANCE TEST ===")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Camera could not be opened.")
    exit()

print("Camera opened successfully!")
print("Obstacle detection started.")
print("Press Q to close.")

while True:
    ret, frame = camera.read()

    if not ret:
        print("ERROR: Could not read camera.")
        break

    frame_height, frame_width = frame.shape[:2]

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    obstacle_count = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore small objects
        if area > 1500:

            x, y, w, h = cv2.boundingRect(contour)

            # Center of object
            center_x = x + w // 2
            center_y = y + h // 2

            # -------------------------
            # LEFT / CENTER / RIGHT
            # -------------------------

            if center_x < frame_width // 3:
                position = "LEFT"

            elif center_x < (frame_width * 2) // 3:
                position = "CENTER"

            else:
                position = "RIGHT"

            # -------------------------
            # NEAR / MEDIUM / FAR
            # -------------------------

            object_size = w * h

            if object_size > 120000:
                distance = "NEAR"

            elif object_size > 40000:
                distance = "MEDIUM"

            else:
                distance = "FAR"

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Draw center point
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Display position
            cv2.putText(
                frame,
                f"{position} - {distance}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            obstacle_count += 1

    # Display object count
    cv2.putText(
        frame,
        f"Objects detected: {obstacle_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Display guide lines
    cv2.line(
        frame,
        (frame_width // 3, 0),
        (frame_width // 3, frame_height),
        (255, 0, 0),
        1
    )

    cv2.line(
        frame,
        ((frame_width * 2) // 3, 0),
        ((frame_width * 2) // 3, frame_height),
        (255, 0, 0),
        1
    )

    # Labels
    cv2.putText(
        frame,
        "LEFT",
        (30, frame_height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "CENTER",
        (frame_width // 2 - 40, frame_height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "RIGHT",
        (frame_width - 100, frame_height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Show camera
    cv2.imshow("SONU-X Obstacle Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Obstacle detection test completed.")