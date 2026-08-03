# Displaying an Image (`imshow` + `waitKey` + `destroyAllWindows`)

These three functions always work together.

---

## `cv2.imshow()`

**Simple:** Opens a window and shows your image.

**Technical:** Creates a named window and renders the image array in it.

**Syntax:**
```python
cv2.imshow(window_title, image)
```

| Parameter | Meaning |
|-----------|---------|
| `window_title` (string) | The window's title bar text |
| `image` | The image array to display |

**Return:** None.

---

## `cv2.waitKey()`

**Simple:** Pauses so the window stays open until you press a key.

**Technical:** Waits n milliseconds for a keyboard event.

**Syntax:**
```python
cv2.waitKey(delay)
```

| Delay | Behavior |
|-------|----------|
| `delay = 0` | Wait **forever** until ANY key is pressed (used for images) |
| `delay = 1` | Wait 1 millisecond, then continue (used for video — checked every frame) |

**Return:** ASCII code of the key pressed, or `-1` if none.

> **Additional Explanation:** Without `waitKey`, the window opens and closes instantly (the program ends before you can see anything). `waitKey` is what makes the window persist. This is the #1 beginner confusion.

---

## `cv2.destroyAllWindows()`

**Simple:** Closes all OpenCV windows cleanly.

**Technical:** Frees the window resources.

**Syntax:**
```python
cv2.destroyAllWindows()   # no arguments
```

---

## Complete Example (`displaying.py`)

```python
import cv2

image = cv2.imread("python.png")

if image is not None:
    cv2.imshow("Image Showing", image)   # open window
    cv2.waitKey(0)                        # wait for a key
    cv2.destroyAllWindows()               # close window
else:
    print("Could not load the image")
```

### Line-by-Line

| Line | Explanation |
|------|-------------|
| `cv2.imshow("Image Showing", image)` | Opens a window titled "Image Showing" displaying `image`. Remove it → nothing shows |
| `cv2.waitKey(0)` | Freezes the window open until a key is pressed. Change `0` to `1` → the window flashes and vanishes instantly (only pauses 1ms). Remove it → same instant-close problem |
| `cv2.destroyAllWindows()` | Closes the window after the key press. Remove it → window may linger / not close cleanly |

---

## Common Mistakes

- Using `imshow` without `waitKey` → window won't display.
- Forgetting `destroyAllWindows` → leftover windows.