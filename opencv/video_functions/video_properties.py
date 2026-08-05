import cv2

# Open the video file
cap = cv2.VideoCapture("/Users/aayushaswal/opencv-yolo-practice/opencv/i-am-inevitable.mp4")

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# ==========================
# Get Video Properties
# ==========================

# Width of each frame (pixels)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# Height of each frame (pixels)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Frames per second
fps = cap.get(cv2.CAP_PROP_FPS)

# Total number of frames in the video
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Duration of the video (seconds)
duration = frame_count / fps if fps > 0 else 0

# ==========================
# Print Properties
# ==========================

print("===== Video Properties =====")
print(f"Frame Width  : {width} pixels")
print(f"Frame Height : {height} pixels")
print(f"FPS          : {fps}")
print(f"Total Frames : {frame_count}")
print(f"Duration     : {duration:.2f} seconds")

# Release the video
cap.release()