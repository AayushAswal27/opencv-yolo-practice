import cv2

# Read image
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/Triangle Picture - Images of Shapes.jpeg")

if image is None:
    print("Error: Could not load image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold (Invert so triangle becomes white)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Number of contours found:", len(contours))

for cnt in contours:

    # Ignore tiny contours (noise)
    if cv2.contourArea(cnt) < 100:
        continue

    # Perimeter
    peri = cv2.arcLength(cnt, True)

    # Approximate contour
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

    corners = len(approx)

    # Shape detection
    if corners == 3:
        shape = "Triangle"

    elif corners == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)

        if 0.95 <= aspect_ratio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"

    elif corners == 5:
        shape = "Pentagon"

    elif corners == 6:
        shape = "Hexagon"

    else:
        shape = "Circle"

    # Draw contour
    cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)

    # Find contour center
    M = cv2.moments(cnt)

    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        cv2.circle(image, (cx, cy), 4, (0, 0, 255), -1)

        cv2.putText(
            image,
            shape,
            (cx - 40, cy),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

# Show results
cv2.imshow("Binary", binary)
cv2.imshow("Detected Shapes", image)

cv2.waitKey(0)
cv2.destroyAllWindows()