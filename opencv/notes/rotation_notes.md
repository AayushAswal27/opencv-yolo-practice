# Function 3: Rotating — `cv2.rotate()` and `cv2.getRotationMatrix2D()` + `cv2.warpAffine()`

Two ways: **quick 90° turns**, or **arbitrary-angle rotation**.

---

## 3a. `cv2.rotate()` — Fixed 90° Rotations

**Simple:** Turn the image in fixed quarter-turns.

**Technical:** Rotates by exactly 90/180/270° with **no interpolation** (just repositions pixels) — fast and lossless.

**Syntax:**
```python
rotated = cv2.rotate(src, rotateCode)
```

**Parameters:**

| Parameter | Meaning |
|-----------|---------|
| `src` | Source image |
| `rotateCode` | One of: `cv2.ROTATE_90_CLOCKWISE`, `cv2.ROTATE_90_COUNTERCLOCKWISE`, `cv2.ROTATE_180` |

**Return:** Rotated image. For 90°/270° the **width and height swap**.

---

## 3b. Arbitrary-Angle Rotation (Any Degree)

This takes **two steps**: build a rotation matrix, then apply it.

### Step 1 — `cv2.getRotationMatrix2D(center, angle, scale)`

**Simple:** Creates the "recipe" for the rotation.

**Technical:** Returns a **2×3 affine transformation matrix** encoding rotation (and optional scaling) around a center point.

| Parameter | Meaning |
|-----------|---------|
| `center` | The point to rotate around, as `(x, y)`. Usually the image center `(width//2, height//2)` |
| `angle` | Degrees. **Positive = counter-clockwise** |
| `scale` | Size multiplier during rotation. `1.0` keeps size |

**Returns:** A 2×3 NumPy matrix.

### Step 2 — `cv2.warpAffine(src, M, dsize)`

**Simple:** Actually applies the rotation recipe to the image.

**Technical:** Applies a 2×3 affine matrix to every pixel, producing the transformed image.

| Parameter | Meaning |
|-----------|---------|
| `src` | Source image |
| `M` | The 2×3 matrix from `getRotationMatrix2D` |
| `dsize` | Output size as `(width, height)` (same order trap as resize) |

**Returns:** The rotated image. Corners may be **clipped** because the output canvas stays the original size.

---

## Common Mistakes

- Using `warpAffine` without first building `M` — there's nothing to apply.
- Expecting no clipping — the simple method keeps the canvas size, so rotated corners get cut. (Fixing that requires computing a larger output size — beyond this phase.)
- Wrong `center` (e.g. `(0,0)`) → image rotates around the corner and swings out of frame.

---

## Best Practices

- Rotate around the **true center** for predictable results.
- For plain 90/180/270°, use `cv2.rotate()` — it's faster and lossless than the matrix method.

---

## Complete Example

```python
import cv2

image = cv2.imread("sample.jpg")
height, width = image.shape[:2]

# Fixed 90 clockwise:
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Arbitrary 45 degrees around center:
center = (width // 2, height // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)            # build the recipe
rotated_45 = cv2.warpAffine(image, M, (width, height))  # apply it

cv2.imshow("90 CW", rotated_90)
cv2.imshow("45 deg", rotated_45)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `center = (width // 2, height // 2)` | The pivot point. Change to `(0, 0)` and the image rotates around its top-left corner, swinging most of it out of view |
| `M = cv2.getRotationMatrix2D(center, 45, 1.0)` | Builds the 2×3 rotation matrix. Change `45` to `-45` and it rotates clockwise instead. Change `1.0` to `0.5` and it rotates AND shrinks to half size |
| `rotated_45 = cv2.warpAffine(image, M, (width, height))` | Executes the rotation. Remove this and `M` is just numbers doing nothing — the matrix is inert until `warpAffine` applies it |

---

## Additional Explanation — What "Affine" Means

An **affine transformation** is one that keeps straight lines straight and parallel lines parallel (rotation, scaling, translation, shear). It's expressed as a **2×3 matrix** multiplied against each pixel's coordinates.

> This is the conceptual cousin of **homography** (Phase 3 of your project) — but homography is a **3×3 matrix** that also handles **perspective** (parallel lines can converge, like railway tracks). Understanding affine here makes homography click faster later.