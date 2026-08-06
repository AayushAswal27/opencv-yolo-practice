# `cv2.drawContours()` — Drawing Contours

**Simple:** Draws the found outlines onto an image so you can see them.

**Technical:** Renders contour boundaries onto an image.

---

## Syntax

```python
cv2.drawContours(img, contours, contourIdx, color, thickness)
```

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `img` | Image to draw on (usually the original color image or a copy) |
| `contours` | The list from `findContours` |
| `contourIdx` | Which contour to draw: an index, or `-1` to draw **ALL** of them |
| `color` | BGR tuple |
| `thickness` | Line width; `-1` **fills** the contour solid |

**Return:** The image (modified **in place** — draw on a copy).

---

## Example

```python
output = image.copy()
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)   # all contours, green
cv2.imshow("Contours", output); cv2.waitKey(0); cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `cv2.drawContours(output, contours, -1, (0,255,0), 2)` | Draws ALL contours in green. Change `-1` to `0` → draws only the first contour. Change thickness to `-1` → fills each shape solid |

---

> **Tip:** Always draw on `image.copy()` — `drawContours` modifies the image in place, so drawing on the original permanently marks it up.