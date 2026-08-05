# `cv2.medianBlur()` — Median Blur

**Simple:** Blurs by replacing each pixel with the **median** of its neighbors. Great at removing "salt-and-pepper" speckle noise.

**Technical:** Replaces each pixel with the median value in its kernel neighborhood — **non-linear**, unlike Gaussian's weighted average.

**Purpose:** Best for removing salt-and-pepper noise (random black/white dots) while preserving edges better than Gaussian.

---

## Syntax

```python
cv2.medianBlur(src, ksize)
```

| Parameter | Meaning |
|-----------|---------|
| `src` | Source image |
| `ksize` | A single **odd integer** (e.g. `5`), **not a tuple**. The kernel is ksize×ksize |

**Return:** Blurred image.

---

## Common Mistakes

- Passing a tuple like `(5,5)` — `medianBlur` wants a single int `5`.
- Even ksize → error.

---

## Example

```python
median = cv2.medianBlur(image, 5)
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `cv2.medianBlur(image, 5)` | 5×5 median filter. Note it's `5`, not `(5,5)` — different from `GaussianBlur`'s tuple. Mixing these up is a common bug |

---

> **Quick contrast:** `GaussianBlur` takes a tuple `(5,5)` · `medianBlur` takes a single int `5`