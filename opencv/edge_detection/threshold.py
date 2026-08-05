import cv2
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg", cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("original image",image)
cv2.imshow("Binary", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()   