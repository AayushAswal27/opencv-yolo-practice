import cv2
image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Found {len(contours)} shapes")

output = image.copy()
cv2.drawContours(output, contours, -1, (0 , 255, 0), 2)   # all contours, green
cv2.imshow("Contours", output); cv2.waitKey(0); cv2.destroyAllWindows()