import cv2

image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")

if image is not None:
    height, width, channels = image.shape
    print(f"Image loaded: Height={height}, Width={width}, Channels={channels}")
else:
    print("Could not load image")