import cv2
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/edge_detection/fabrice-villard-Jrl_UQcZqOc-unsplash.jpg", 0)
edges = cv2.Canny(image, 100, 200)
cv2.imshow("original image",image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows() 