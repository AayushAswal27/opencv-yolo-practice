import cv2

image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")   # load (default = color)

if image is None:
    print("Error: Image not found, check file path")
else:
    print("Image loaded successfully")