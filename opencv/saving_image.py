import cv2

image = cv2.imread("/Users/aayushaswal/opencv-yolo-practice/opencv/1013802.jpg")

if image is not None:
    success = cv2.imwrite("edited_image.jpg", image)
    if success:
        print("Image saved successfully as 'output_python.png'")
    else:
        print("Failed to save image")
else:
    print("Error: could not load image")