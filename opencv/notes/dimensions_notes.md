# Attribute: `.shape` — Image Dimensions

**Simple:** Tells you the image's height, width, and number of color channels.

**Technical:** `.shape` is a NumPy attribute (**NOT** a function/method — no parentheses) that returns the array's dimensions.

---

## Syntax

```python
height, width, channels = image.shape
```

---

## What It Returns (a tuple)

| Image Type | Returns | Example |
|------------|---------|---------|
| **Color image** | `(height, width, channels)` | `(336, 568, 3)` |
| **Grayscale image** | `(height, width)` | 3rd value is MISSING (only 2 values) |

- **Grayscale detection:** only 2 values returned → this is how you detect grayscale.
- `channels == 3` → BGR color image.

---

## Complete Example (`dimensions.py`)

```python
import cv2

image = cv2.imread("python.png")

if image is not None:
    height, width, channels = image.shape
    print(f"Image loaded: Height={height}, Width={width}, Channels={channels}")
else:
    print("Could not load image")
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `height, width, channels = image.shape` | Unpacks the tuple into 3 variables. If the image were grayscale, `.shape` returns only 2 values and this line **CRASHES** with a "not enough values to unpack" error. (Handle grayscale separately.) |

---

## Warehouse Project Link

> will use `.shape` constantly — resizing frames to YOLO's input size, computing homography scaling, checking whether a loaded image is color or grayscale.
>
> It's also where the **width-vs-height ordering trap** starts: `.shape` gives `(height, width)`, but `cv2.resize` wants `(width, height)`. 

---

> **Additional Explanation:** `.shape` has no parentheses because it's an **attribute** (stored property), not a **method** (function you call).
>
> `image.shape` ✅ &nbsp;&nbsp; `image.shape()` ❌ (TypeError)