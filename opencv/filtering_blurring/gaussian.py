import cv2
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")
blur = cv2.GaussianBlur(image, (21,21),0)
cv2.imshow("Original image",image)
cv2.imshow("Gaussian", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()