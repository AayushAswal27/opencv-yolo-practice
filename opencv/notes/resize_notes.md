# `cv2.resize()` — Resizing / Scaling

**Simple:** Makes an image bigger or smaller.

**Technical:** Recomputes the pixel grid at a new width/height using an **interpolation** algorithm to decide the new pixel values.

**Purpose:** Models expect a fixed input size (YOLO wants e.g. 640×640). Displays need images to fit. Smaller images process faster. Resizing is one of the most-used operations in all of CV.

---

## Syntax

```python
resized = cv2.resize(src, dsize, fx, fy, interpolation)
```

---

## Parameters

| Parameter | Meaning |
|-----------|---------|
| `src` (required) | The source image array |
| `dsize` (required-ish) | Target size as `(width, height)`. **The trap:** this is the REVERSE of `.shape`'s `(height, width)`. Pass `None` here if you'd rather scale by factor |
| `fx` (optional) | Horizontal scale factor (used when `dsize=None`). e.g. `0.5` = half width |
| `fy` (optional) | Vertical scale factor. e.g. `0.5` = half height |
| `interpolation` (optional) | The resampling method (see below) |

### Interpolation Methods
| Method | Best For |
|--------|----------|
| `cv2.INTER_AREA` | **Shrinking** |
| `cv2.INTER_LINEAR` | Default, good general-purpose / enlarging |
| `cv2.INTER_CUBIC` | Slower, higher quality when enlarging |

**Return value:** A new resized image. The original is untouched.

---

## How It Works Internally

- **When shrinking:** multiple source pixels map to one output pixel → OpenCV averages them (that's why `INTER_AREA` is best for shrinking, it avoids aliasing).
- **When enlarging:** output pixels fall between source pixels, so OpenCV interpolates (estimates) the in-between values — linearly or cubically.

---

## Common Mistakes

- Passing `(height, width)` instead of `(width, height)` → image squished the wrong way. **The #1 resize bug.**
- Using `INTER_LINEAR` to shrink a lot → slightly blurry/aliased result (use `INTER_AREA`).
- Forgetting resize returns a **new** image and expecting the original to change.

---

## Best Practices

- Match `interpolation` to the operation: `INTER_AREA` down, `INTER_CUBIC`/`INTER_LINEAR` up.
- When you only care about proportion, use `fx`/`fy` with `dsize=None` to avoid the width/height mixup entirely.

---

## Complete Example

```python
import cv2

image = cv2.imread("sample.jpg")

# Exact size (WIDTH, HEIGHT):
resized_exact = cv2.resize(image, (300, 200), interpolation=cv2.INTER_AREA)

# By scale factor (half size):
resized_half = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("Exact 300x200", resized_exact)
cv2.imshow("Half size", resized_half)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `cv2.resize(image, (300, 200), ...)` | Produces a 300-wide, 200-tall image. Swap to `(200, 300)` and you get a 200×300 image — a different shape. Get this order wrong and every downstream size assumption breaks |
| `cv2.resize(image, None, fx=0.5, fy=0.5, ...)` | Halves both dimensions. Remove `None` / provide a dsize AND fx/fy and dsize wins; fx/fy are ignored |

---

## Warehouse Project Link

> Before YOLO inference you resize frames to the model's expected input. Getting `(width, height)` order right here matters because your homography coordinate math later assumes a known frame size.

---

> **Additional Explanation:** "Interpolation" just means "estimating unknown values between known ones." When you blow a 100×100 image up to 400×400, 15 out of every 16 output pixels didn't exist in the original — interpolation invents them from neighbors. That's why heavily-enlarged images look soft: you can't create real detail that was never captured.