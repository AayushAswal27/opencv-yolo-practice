# Contours & Shape Detection

**Goal:** Find the outlines of objects (contours), draw them, and identify basic shapes (triangle, square, circle) by analyzing those outlines.

> In your project YOLO handles object detection, but contours are still useful for things like isolating a floor region, measuring areas, or classical fallback analysis — and this phase teaches how shape/area reasoning works, which underpins a lot of CV.

---

## The One Idea Behind Contours

**Simple:** A contour is a continuous curve that traces the boundary of a shape — like drawing an outline around an object.

**Technical:** A contour is a list of `(x, y)` points along the boundary of a connected white region in a binary image. OpenCV finds these boundaries and returns them as arrays of points you can measure, draw, or classify.

### The Workflow Is Always:

```
1. Load image
2. Convert to grayscale
3. Threshold (or Canny) -> binary image   ← contours need black/white input
4. findContours -> get the outlines
5. drawContours / analyze each contour
```

> Contours only work on **binary images** (black & white), which is why Phase 6 (thresholding) comes first — it's the prerequisite.

---

## Function 1: `cv2.findContours()` — Finding Contours

**Simple:** Detects all the object outlines in a binary image.

**Technical:** Traces the boundaries of connected white regions and returns them as lists of boundary points.

**Purpose:** The core step — extract every shape's outline so you can count objects, measure areas, or classify shapes.

---

### Syntax

```python
contours, hierarchy = cv2.findContours(src, mode, method)
```

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `src` | A **binary image** (from threshold or Canny). **Not a color image** |
| `mode` | How contours are retrieved (see below) |
| `method` | How boundary points are stored (see below) |

### `mode` Options
| Mode | Effect |
|------|--------|
| `cv2.RETR_EXTERNAL` | Only the outermost contours (most common; ignores holes inside shapes) |
| `cv2.RETR_LIST` | All contours, no hierarchy |
| `cv2.RETR_TREE` | All contours with full parent/child hierarchy |

### `method` Options
| Method | Effect |
|--------|--------|
| `cv2.CHAIN_APPROX_SIMPLE` | Compresses straight segments (stores only corners; memory-efficient; most common) |
| `cv2.CHAIN_APPROX_NONE` | Stores every single boundary point |

### Return Value (TWO things)
| Variable | Meaning |
|----------|---------|
| `contours` | A list; each element is one contour (a NumPy array of its boundary points) |
| `hierarchy` | Info about nested contours (parent/child relationships). Often ignored |

**How it works internally:** It scans the binary image and follows the borders between white and black regions, recording the coordinate points along each border.

---

### Common Mistakes

- Passing a color/grayscale (non-binary) image → wrong or no contours. **Threshold first.**
- Forgetting it returns two values (`contours, hierarchy`).

> **⚠️ Version note:** Older OpenCV (v3) returned **three** values (`image, contours, hierarchy`). OpenCV 4.x (yours) returns **two**. Tutorials showing three values are outdated.

---

### Best Practices

- Use `RETR_EXTERNAL` + `CHAIN_APPROX_SIMPLE` for typical object detection.
- Clean the binary image (blur/threshold well) before finding contours to avoid noise contours.

---

### Example

```python
import cv2
image = cv2.imread("shapes.jpg")
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary,
                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Found {len(contours)} shapes")
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `ret, binary = cv2.threshold(...)` | Make the binary image contours require. Skip this and pass `gray` directly → contours are unreliable or empty |
| `cv2.findContours(binary, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)` | Get outer outlines, corners only. Change to `RETR_TREE` and you also get inner contours (holes); change to `CHAIN_APPROX_NONE` and each contour stores far more points |
| `len(contours)` | Counts detected shapes. This is literally "counting objects" — the classical version of what YOLO does with detections |