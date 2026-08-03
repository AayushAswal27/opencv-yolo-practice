import cv2
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")
canvas = image.copy()
cv2.rectangle(canvas, (50, 50), (200, 200), (0, 255, 0), 2)   
cv2.imshow("Rect", canvas); cv2.waitKey(0)
cv2.destroyAllWindows() 