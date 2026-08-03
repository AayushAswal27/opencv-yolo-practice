import cv2

image = cv2.imread("opencv/1013802.jpg")

if image is not None:
    cropped=image[200:500,200:400]
    print("Image loaded")
    # Show original image
    cv2.imshow("Original Image", image)
    # Show resized image
    cv2.imshow("cropped Image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()