# `cv2.flip()` — Flipping / Mirroring

**Simple:** Mirror the image horizontally or vertically.

**Technical:** Reverses pixel order along one or both axes.

**Purpose:** Data augmentation (flipping training images to double your dataset variety — very relevant when you train YOLO), mirror effects, correcting selfie-flipped webcam feeds.

---

## Syntax

```python
flipped = cv2.flip(src, flipCode)
```

---

## Parameters

| Parameter | Meaning |
|-----------|---------|
| `src` | Source image |
| `flipCode` | Which axis to flip along (see below) |

### Flip Codes
| Code | Effect |
|------|--------|
| `1` | Horizontal flip (mirror left↔right) |
| `0` | Vertical flip (upside down) |
| `-1` | Both axes |

**Return:** The flipped image.

---

## Common Mistakes

- Mixing up `0` and `1` (vertical vs horizontal) — easy to swap; just test and see.

---

## Best Practices

- Horizontal flip (`1`) is the **standard, safe augmentation** for most object detection.
- Vertical flips can be wrong for some data (an upside-down forklift isn't realistic training data).

> Keep this in mind when augmenting your warehouse set.

---

## Complete Example

```python
import cv2

image = cv2.imread("sample.jpg")

flip_h = cv2.flip(image, 1)   # mirror L-R
flip_v = cv2.flip(image, 0)   # upside down

cv2.imshow("Horizontal", flip_h)
cv2.imshow("Vertical", flip_v)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `cv2.flip(image, 1)` | Horizontal mirror. Change `1` to `0` and it flips top-to-bottom instead; `-1` does both at once |