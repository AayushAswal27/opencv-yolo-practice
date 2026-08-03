# `cv2.imwrite()` — Saving an Image

**Simple:** Saves an (edited) image to your hard drive.

**Technical:** Encodes the image array to the chosen format and writes it to disk.

**Purpose:** After you edit/filter/convert an image, you must save it to keep the result.

> **Analogy:** Editing a photo on your phone is useless until you hit Save.

---

## Syntax

```python
success = cv2.imwrite(filename, image)
```

---

## Parameters

| Parameter | Meaning |
|-----------|---------|
| `filename` (string) | Output name with extension (e.g. `output.jpg`). The **extension decides the format** |
| `image` | The array to save |

**Return value:** `True` if saved successfully, `False` if it failed.

---

## Complete Example (`saving.py`)

```python
import cv2

image = cv2.imread("python.png")

if image is not None:
    success = cv2.imwrite("output_python.png", image)
    if success:
        print("Image saved successfully as output_python.png")
    else:
        print("Failed to save image")
else:
    print("Error: could not load image")
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `success = cv2.imwrite("output_python.png", image)` | Writes `image` to disk as PNG; `success` captures True/False. If you omit the extension, OpenCV won't know the format and the save fails |
| `if success:` | Reports the outcome. The True/False return is your **only signal** the save worked — check it |

---

## Warehouse Project Link

> This is how will be saving annotated output frames, cropped detections, and processed video frames in your pipeline.