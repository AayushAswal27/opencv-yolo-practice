# `cv2.threshold()` — Binary Thresholding

**Simple:** Turns an image pure black-and-white — pixels above a cutoff become white, below become black.

**Technical:** Applies a fixed **global threshold**: each pixel compared to a value, set to max or 0 based on the rule.

**Purpose:** Isolate objects from background, create masks, prep for contour detection. Foundational for segmentation.

---

## Syntax

```python
ret, thresh = cv2.threshold(src, thresh, maxval, type)
```

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `src` | Source (usually grayscale) |
| `thresh` | The cutoff value (0–255) |
| `maxval` | Value assigned to pixels that pass (usually 255 = white) |
| `type` | The rule (see below) |

### Threshold Types
| Type | Effect |
|------|--------|
| `cv2.THRESH_BINARY` | Above thresh → maxval, else 0 |
| `cv2.THRESH_BINARY_INV` | Inverted |
| `cv2.THRESH_OTSU` | Auto-computes the best threshold (combine with BINARY) |

### Return Value (TWO things)
| Variable | Meaning |
|----------|---------|
| `ret` | The threshold used (useful with OTSU, which computes it) |
| `thresh` | The resulting binary image |

### Common Mistakes
- Forgetting it returns two values (`ret, thresh`).
- Applying to a color image — threshold expects grayscale.

### Example
```python
import cv2
image = cv2.imread("sample.jpg", 0)
ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", thresh); cv2.waitKey(0); cv2.destroyAllWindows()
```

### Line-by-Line
| Line | Explanation |
|------|-------------|
| `ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)` | Pixels >127 become white(255), rest black. Change `127` to `200` → only very bright pixels survive (mostly black image). Change type to `THRESH_BINARY_INV` → colors flip |

---

# Function 3: `cv2.adaptiveThreshold()` — Adaptive Thresholding

**Simple:** Like thresholding, but the cutoff **adjusts locally** across the image — great when lighting is uneven.

**Technical:** Computes a different threshold for each region based on local neighborhood statistics.

**Purpose:** Handle images with varying lighting/shadows where a single global threshold fails (e.g. a document photographed with uneven light).

> Warehouse footage has uneven lighting — adaptive handles that better than global.

---

## Syntax

```python
thresh = cv2.adaptiveThreshold(src, maxval, adaptiveMethod, thresholdType, blockSize, C)
```

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `src` | Grayscale source |
| `maxval` | Value for passing pixels (255) |
| `adaptiveMethod` | `cv2.ADAPTIVE_THRESH_MEAN_C` or `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` (how local threshold is computed) |
| `thresholdType` | `cv2.THRESH_BINARY` or `_INV` |
| `blockSize` | Size of the local region (**odd** number, e.g. 11) |
| `C` | A constant subtracted from the computed mean (fine-tuning) |

**Return:** The binary image (just **one** value, unlike `threshold`).

### Example
```python
thresh = cv2.adaptiveThreshold(image, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
```

### Common Mistakes
- Even `blockSize` → error (must be odd).
- Expecting a `ret` return like `threshold` — adaptive returns **only the image**.

---

> **Quick contrast:** `threshold` → one global cutoff, returns `ret, thresh` (2 values) · `adaptiveThreshold` → local cutoffs, returns just the image (1 value)