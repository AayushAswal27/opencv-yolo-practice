# Edge Detection & Thresholding

**Goal:** Find edges (Canny), convert images to pure black/white (thresholding), and combine images with bitwise logic.

> Thresholding and masks are how you isolate regions; edges are a classic feature. The instructor flags this as the **most interview-heavy phase**.

---

## Function 1: `cv2.Canny()` — Edge Detection

**Simple:** Finds the outlines/edges in an image (where brightness changes sharply).

**Technical:** The Canny algorithm detects edges via gradient computation, non-maximum suppression, and double-thresholding with hysteresis. Output is a **binary image**: white edges on black.

**Purpose:** Extract object outlines, feature for shape detection, pre-step for contour finding.

---

## Syntax

```python
edges = cv2.Canny(src, threshold1, threshold2)
```

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `src` | Source image (usually grayscale, often blurred first) |
| `threshold1` | **Lower threshold** — edges weaker than this are discarded |
| `threshold2` | **Upper threshold** — edges stronger than this are definitely kept |

> **Between the two:** kept only if connected to a strong edge (**hysteresis**).

**Return:** A binary edge image (white edges, black background).

---

## How It Works Internally (The 4 Steps — Good Interview Material)

1. **Noise reduction** — Gaussian blur (why you blur first).
2. **Gradient calculation** — find intensity changes (Sobel) → edge strength + direction.
3. **Non-maximum suppression** — thin thick edges to 1-pixel lines.
4. **Double threshold + hysteresis** — classify strong/weak edges; keep weak ones only if connected to strong ones.

---

## Common Mistakes

- Not blurring first → noisy, broken edges.
- Bad thresholds → too many or too few edges. Common start: `Canny(img, 100, 200)`.

---

## Example

```python
import cv2
image = cv2.imread("sample.jpg", 0)          # grayscale
blur  = cv2.GaussianBlur(image, (5,5), 0)
edges = cv2.Canny(blur, 100, 200)
cv2.imshow("Edges", edges); cv2.waitKey(0); cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `cv2.Canny(blur, 100, 200)` | Edges with low=100, high=200. Lower both (e.g. 50,100) → more edges (and more noise). Raise them → fewer, only the strongest edges. Skip the blur line → noisier, more broken edges |