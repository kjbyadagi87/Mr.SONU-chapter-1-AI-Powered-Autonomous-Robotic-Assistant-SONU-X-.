import cv2

print("=== SONU-X AUTONOMOUS DECISION TEST ===")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Camera could not be opened.")
    exit()

print("Camera opened successfully!")
print("Autonomous decision system started.")
print("Press Q to close.")


while True:

    ret, frame = camera.read()

    if not ret:
        print("ERROR: Could not read camera.")
        break

    # Resize camera frame
    frame = cv2.resize(frame, (640, 480))

    # Get frame dimensions
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

    # Default decision
    decision = "MOVE FORWARD"
    detected_position = "NONE"
    detected_distance = "NONE"

    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore small objects
        if area > 1500:

            x, y, w, h = cv2.boundingRect(contour)

            # Object center
            center_x = x + w // 2
            center_y = y + h // 2

            # -------------------------
            # POSITION
            # -------------------------

            if center_x < frame_width // 3:
                position = "LEFT"

            elif center_x < (frame_width * 2) // 3:
                position = "CENTER"

            else:
                position = "RIGHT"

            # -------------------------
            # DISTANCE ESTIMATION
            # -------------------------

            object_size = w * h

            if object_size > 120000:
                distance = "NEAR"

            elif object_size > 40000:
                distance = "MEDIUM"

            else:
                distance = "FAR"

            detected_position = position
            detected_distance = distance

            # -------------------------
            # SONU-X DECISION
            # -------------------------

            if distance == "NEAR":

                if position == "CENTER":
                    decision = "STOP"

                elif position == "LEFT":
                    decision = "TURN RIGHT"

                elif position == "RIGHT":
                    decision = "TURN LEFT"

            elif distance == "MEDIUM":

                if position == "CENTER":
                    decision = "SLOW DOWN"

                elif position == "LEFT":
                    decision = "MOVE RIGHT"

                elif position == "RIGHT":
                    decision = "MOVE LEFT"

            else:

                decision = "MOVE FORWARD"

            # -------------------------
            # DRAW OBJECT
            # -------------------------

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Center point
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Object information
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

    # -------------------------
    # DISPLAY INFORMATION
    # -------------------------

    cv2.putText(
        frame,
        f"Objects: {obstacle_count}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Position: {detected_position}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Distance: {detected_distance}",
        (20, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # BIG SONU-X DECISION
    cv2.putText(
        frame,
        f"DECISION: {decision}",
        (20, 145),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # -------------------------
    # LEFT / CENTER / RIGHT
    # -------------------------

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

    # Show camera
    cv2.imshow(
        "SONU-X Autonomous Decision System",
        frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()

print("SONU-X autonomous decision test completed.")