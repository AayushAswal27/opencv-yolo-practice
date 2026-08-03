import cv2

image = cv2.imread("opencv/1013802.jpg")


if image is None:
    print("could not able to load image")
else:
    flip_h = cv2.flip(image, 1)   
    flip_v = cv2.flip(image, 0)   
    flip_b = cv2.flip(image,-1)
    cv2.imshow("original image ",image)
    cv2.imshow("Horizontal image ", flip_h)
    cv2.imshow("Vertical image ", flip_v)
    cv2.imshow("flipped-both image ", flip_b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
