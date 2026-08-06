# Shape Detection with `cv2.approxPolyDP()` + `cv2.arcLength()`

This is how you identify **what shape** a contour is (triangle, square, circle) — by **counting its corners**.

---

## `cv2.arcLength()` — Measure a Contour's Perimeter

**Simple:** Measures the length around a contour.

**Syntax:**
```python
perimeter = cv2.arcLength(contour, closed)
```

| Parameter | Meaning |
|-----------|---------|
| `contour` | One contour |
| `closed` | `True` if the shape is a closed loop |

**Return:** The perimeter length (float). Used to scale the approximation below.

---

## `cv2.approxPolyDP()` — Simplify a Contour to Its Corners

**Simple:** Reduces a contour to a simpler polygon — smooths out the many boundary points into just the essential corners.

**Technical:** Applies the **Douglas-Peucker algorithm** to approximate a contour with fewer vertices within a tolerance.

**Purpose:** Shape classification — the number of resulting corners tells you the shape: **3 = triangle, 4 = square/rectangle, many = circle.**

### Syntax
```python
approx = cv2.approxPolyDP(contour, epsilon, closed)
```

### Parameters
| Parameter | Meaning |
|-----------|---------|
| `contour` | The contour to simplify |
| `epsilon` | Approximation accuracy (max distance from original curve). Usually a fraction of the perimeter, e.g. `0.02 * arcLength`. Smaller = more faithful (more points); larger = simpler |
| `closed` | `True` for closed shapes |

**Return:** A simplified array of corner points. `len(approx)` = number of corners.

**How it works internally (Douglas-Peucker):** It repeatedly keeps the points that deviate most from a straight line and discards points that lie nearly on straight segments — collapsing a many-point curve into just its defining corners.

---

## Complete Shape-Detection Example

```python
import cv2
image = cv2.imread("shapes.jpg")
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    peri   = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    corners = len(approx)

    if corners == 3:
        shape = "Triangle"
    elif corners == 4:
        shape = "Square/Rectangle"
    elif corners > 6:
        shape = "Circle"
    else:
        shape = "Polygon"

    # label the shape at its first corner
    x, y = approx[0][0]
    cv2.putText(image, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
    cv2.drawContours(image, [cnt], -1, (0,255,0), 2)

cv2.imshow("Shapes", image); cv2.waitKey(0); cv2.destroyAllWindows()
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `peri = cv2.arcLength(cnt, True)` | Perimeter, used to scale epsilon |
| `approx = cv2.approxPolyDP(cnt, 0.02*peri, True)` | Simplify to corners. Change `0.02` to `0.1` → over-simplifies (a square might collapse to a triangle); change to `0.001` → barely simplifies (a square keeps dozens of points and never reads as "4 corners"). `0.02` is the sweet spot |
| `corners = len(approx)` | The corner count **IS** the shape identifier. This is the whole trick: count corners → name the shape |

---

# Object Recognition Basics (Bounding Boxes from Contours)

Drawing bounding boxes around contours — the classical precursor to YOLO's boxes.

---

## `cv2.boundingRect(contour)` — Get the Upright Bounding Box

- **Returns:** `(x, y, w, h)` — top-left corner + width + height.
- Draw it with `cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)`.

### Example
```python
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
```

> **Warehouse Project Link:** This `(x, y, w, h)` box + `cv2.rectangle` is **exactly the format YOLO gives you per detection**. Contours draw boxes from shape outlines; YOLO draws them from a trained model — but the drawing and the box format are identical. Understanding this makes YOLO's output feel familiar.

---

## `cv2.contourArea(contour)` — Get the Area (Pixel Count)

- Useful to **filter out tiny noise contours**:
```python
if cv2.contourArea(cnt) < 500:
    continue
```