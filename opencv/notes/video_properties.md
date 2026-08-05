# Getting Video Properties — `cap.get()`

**Simple:** Ask the video about itself — its width, height, FPS, frame count.

**Technical:** Retrieves a property of the capture source by property ID.

---

## Syntax

```python
value = cap.get(propId)
```

---

## Common Property IDs

| Property ID | Meaning |
|-------------|---------|
| `cv2.CAP_PROP_FRAME_WIDTH` | Frame width in pixels |
| `cv2.CAP_PROP_FRAME_HEIGHT` | Frame height in pixels |
| `cv2.CAP_PROP_FPS` | Frames per second |
| `cv2.CAP_PROP_FRAME_COUNT` | Total frames (for files) |

**Return value:** A float (cast to `int` when you need pixel dimensions).

---

## Example

```python
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)
print(f"{width}x{height} @ {fps} FPS")
```

---

## Warehouse Project

> You need width/height/FPS to set up your `VideoWriter` (below) so the saved output matches the input.
>
> FPS matters for your **collision math**: velocity = distance / time, and time-per-frame = 1/FPS.