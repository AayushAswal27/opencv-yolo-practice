import cv2

cap = cv2.VideoCapture("/Users/aayushaswal/opencv-yolo-practice/opencv/i-am-inevitable.mp4")

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --- process frame here (e.g. grayscale, or later: YOLO) ---
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # back to 3-channel to save

    out.write(gray_bgr)                # write the processed frame
    cv2.imshow("Processing", gray_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()                          # IMPORTANT: finalizes the file
cv2.destroyAllWindows()