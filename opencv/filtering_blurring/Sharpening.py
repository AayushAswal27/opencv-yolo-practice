import cv2,numpy as np
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharp = cv2.filter2D(image, -1, kernel)
cv2.imshow("Original Image",image)
cv2.imshow("Sharpened", sharp); cv2.waitKey(0); cv2.destroyAllWindows()
