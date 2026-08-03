# Cropping (NumPy Slicing — No OpenCV Function)

**Simple:** Cut out a rectangular piece of the image.

**Technical:** Because the image is a NumPy array, you crop by **slicing rows and columns** — no OpenCV function needed.

**Purpose:** Focus on a region of interest (cropping a detected worker or forklift out of a frame to feed a re-ID model in Phase 6). Remove irrelevant borders. Zoom into a zone.

---

## Syntax

```python
crop = image[y1:y2, x1:x2]
```

---

## Parameters (slice ranges)

| Slice | Meaning |
|-------|---------|
| `y1:y2` | Rows = the vertical (height) range |
| `x1:x2` | Columns = the horizontal (width) range |

> **Order is `[rows, cols]` = `[y, x]`** — the opposite of how we usually say "(x, y)". This matches `.shape` being `(height, width)`.

**Return value:** A view/sub-array of the original (a smaller image).

> **Note:** A plain slice is a **view** — modifying it can affect the original. Use `.copy()` if you need an independent crop.

---

## Common Mistakes

- Writing `[x1:x2, y1:y2]` (x first) → you crop the wrong axis and get an unexpected region.
- Forgetting a slice is a view, then accidentally editing the original through it.
- Going out of bounds — NumPy silently **clips** instead of erroring, giving a smaller crop than expected.

---

## Best Practices

- Say it to yourself as **"rows then columns, y then x"** every time.
- Use `image[y1:y2, x1:x2].copy()` when the crop will be modified independently.

---

## Complete Example

```python
import cv2

image = cv2.imread("sample.jpg")

# Top-left 200x200 box:
crop = image[0:200, 0:200]        # rows 0-200, cols 0-200

cv2.imshow("Cropped 200x200", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `crop = image[0:200, 0:200]` | Selects the first 200 rows and first 200 columns. Change to `image[0:200]` (rows only) and you keep ALL columns → a full-width horizontal strip. Reverse the ranges' meaning by thinking x-first and you'll crop the wrong part of the image |

---

## Warehouse Project Link

> In warehouse project , re-ID works by cropping each detected person out of the frame (using YOLO's bounding box as the slice coordinates) and turning that crop into an appearance embedding. This slice is literally how you extract a worker from a frame.