# Bitwise Operations — `cv2.bitwise_and/or/not/xor()`

**Simple:** Combine two images (or an image and a mask) using logical operations — useful for masking regions in/out.

**Technical:** Perform pixel-wise boolean logic between images/masks.

**Purpose:** Masking — keep only part of an image (e.g. only a detected region), overlay logos, isolate colors. Core to region-of-interest work.

---

## The Four Operations

| Operation | Effect |
|-----------|--------|
| `cv2.bitwise_and(img1, img2, mask=...)` | Keeps pixels where **BOTH** are set (masking's workhorse) |
| `cv2.bitwise_or(img1, img2)` | Keeps pixels where **EITHER** is set |
| `cv2.bitwise_not(img)` | **Inverts** (white↔black) |
| `cv2.bitwise_xor(img1, img2)` | Keeps where they **DIFFER** |

---

## Syntax (AND)

```python
result = cv2.bitwise_and(img1, img2, mask=mask)
```

| Parameter | Meaning |
|-----------|---------|
| `img1, img2` | Input images (same size) |
| `mask` (optional) | A binary image; operation only applies where mask is white |

**Return:** The combined image.

---

## Example — Masking with a Threshold

```python
import cv2
image = cv2.imread("sample.jpg")
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# keep only the parts of the original where mask is white:
result = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked", result); cv2.waitKey(0); cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `mask = cv2.threshold(...)` | Build a black/white mask |
| `cv2.bitwise_and(image, image, mask=mask)` | Keeps original pixels only where mask is white; rest becomes black. This is the fundamental **"show only this region"** pattern. You'd use this to isolate a detected zone or region of interest |

---

## Additional Explanation — What "Bitwise" Means

Each pixel value is stored in **binary (bits)**. "Bitwise AND" compares the bits of corresponding pixels.

With a 0/255 mask, `and` acts like a **stencil**:
- Where the mask is **255** (all bits 1), the original pixel **passes through**.
- Where it's **0**, the pixel is **zeroed out (black)**.

> That's why bitwise ops + masks = precise region control.