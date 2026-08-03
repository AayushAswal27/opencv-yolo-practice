import cv2

image = cv2.imread("opencv/1013802.jpg")
height, width = image.shape[:2]

center = (width // 2, height // 2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)    
rotated = cv2.warpAffine(image, M, (width, height)) 

cv2.imshow("original image", image)
cv2.imshow("rotated 90 degree", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()