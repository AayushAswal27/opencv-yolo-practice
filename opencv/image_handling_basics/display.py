
import cv2

image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")

if image is not None:
    cv2.imshow("Image Showing", image)   # open window
    cv2.waitKey(0)                        # wait for a key
    cv2.destroyAllWindows()               # close window
else:
    print("Could not load the image")

