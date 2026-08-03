import cv2

image = cv2.imread("opencv/1013802.jpg")

if image is None:
    print("Image not found")
else:
    print("Image loaded")
    # Exact size (WIDTH, HEIGHT):
    resized = cv2.resize(image, (300, 300))

    # Show original image
    cv2.imshow("Original Image", image)

    # Show resized image
    cv2.imshow("Resized Image", resized)

    # Save resized image
    cv2.imwrite("resized_image.jpg", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()