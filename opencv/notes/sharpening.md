# Sharpening (Custom Kernel + `cv2.filter2D()`)

**Simple:** Makes edges/details crisper — the opposite of blur.

**Technical:** Applies a custom kernel that boosts the center pixel relative to its neighbors, emphasizing edges.

---

## Two Functions Involved

### 1. `np.array(...)` — Define the Sharpening Kernel Manually

```python
import numpy as np
kernel = np.array([[ 0, -1,  0],
                   [-1,  5, -1],
                   [ 0, -1,  0]])
```

> This kernel **amplifies the center (5)** and **subtracts neighbors (-1)** → enhances edges.

### 2. `cv2.filter2D(src, ddepth, kernel)` — Apply ANY Custom Kernel

| Parameter | Meaning |
|-----------|---------|
| `src` | Source image |
| `ddepth` | Output image depth; `-1` means "same as source". (Depth = the data type/bit-depth of pixels) |
| `kernel` | Your custom kernel matrix |

**Return:** Filtered image.

---

## Example

```python
import cv2, numpy as np
image = cv2.imread("sample.jpg")
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharp = cv2.filter2D(image, -1, kernel)
cv2.imshow("Sharpened", sharp); cv2.waitKey(0); cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `kernel = np.array([...])` | The sharpening recipe. Change the center `5` to `9` (and neighbors to make it sum right) for stronger sharpening. Make all values positive and equal → it becomes a blur instead |
| `cv2.filter2D(image, -1, kernel)` | Applies the kernel. `filter2D` is the **general tool**: ANY effect (blur, sharpen, edge) is just a different kernel here |

---

## Warehouse Project Link

> `cv2.filter2D` applying a kernel is **exactly what a CNN conv layer does** — except the CNN's kernel values are **learned** during training instead of hand-designed. This is your bridge from OpenCV → deep learning.