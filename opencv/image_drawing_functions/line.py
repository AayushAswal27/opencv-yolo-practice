import cv2
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")
canvas = image.copy()
cv2.line(canvas, (200,600), (100,500), (0, 0, 255), 3)   # red diagonal
cv2.imshow("Line", canvas)
cv2.waitKey(0); cv2.destroyAllWindows()