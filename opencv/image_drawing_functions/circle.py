import cv2
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")
canvas = image.copy()
cv2.circle(canvas, (1600,1600), 500, (255, 0, 0), 2)   # blue outline
cv2.imshow("Circle", canvas)
cv2.waitKey(0); cv2.destroyAllWindows()