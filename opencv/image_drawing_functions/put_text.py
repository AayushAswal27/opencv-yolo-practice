import cv2
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")
canvas = image.copy()
cv2.putText(canvas, "I am Iron Man", (200, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
cv2.imshow("Text", canvas); cv2.waitKey(0); cv2.destroyAllWindows()