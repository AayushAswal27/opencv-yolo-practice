# `cv2.VideoWriter()` — Saving Processed Video

**Simple:** Saves your processed frames into a new video file.

**Technical:** Creates a writer object that encodes frames and writes them to disk as a video.

**Purpose:** Directly your project — after drawing boxes, IDs, and alerts on each frame, you write them to an output video. That output video (with detections baked in) becomes your demo GIF / dashboard playback.

---

## Syntax

```python
out = cv2.VideoWriter(filename, fourcc, fps, frameSize)
```

---

## Parameters

| Parameter | Meaning |
|-----------|---------|
| `filename` | Output name, e.g. `"output.mp4"` or `"output.avi"`. Extension + fourcc decide the format |
| `fourcc` | The codec (compression format), created with `cv2.VideoWriter_fourcc(*'mp4v')` (for .mp4) or `*'XVID'` (for .avi). A 4-character code telling OpenCV how to encode |
| `fps` | Frames per second of the output (usually match the input's FPS) |
| `frameSize` | `(width, height)` tuple. **Same order trap:** `(width, height)`, and it must match the size of the frames you write, or the output is corrupted/empty |

**Return value:** A `VideoWriter` object. You feed frames to it with `out.write(frame)`.

### Companion Method — `out.write(frame)`
- Writes one processed frame to the output file. Called once per loop iteration.
- The frame's size **must match** the `frameSize` you set, or the write silently fails/corrupts.

---

## Full Save Example

```python
import cv2

cap = cv2.VideoCapture("input.mp4")

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --- process frame here (e.g. grayscale, or later: YOLO) ---
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # back to 3-channel to save

    out.write(gray_bgr)                # write the processed frame
    cv2.imshow("Processing", gray_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()                          # IMPORTANT: finalizes the file
cv2.destroyAllWindows()
```

---

## Common Mistakes

- `frameSize` not matching the actual frame size → empty or corrupt output. If you resize frames, set `frameSize` to the resized dimensions.
- Writing a grayscale (1-channel) frame to a writer expecting 3 channels → fails. Convert back to BGR before writing (as above).
- Forgetting `out.release()` → the video file is incomplete/unplayable (the writer needs to finalize the file).
- Wrong fourcc for the extension (e.g. `mp4v` codec with `.avi` name) → may not write.

---

## Best Practices

- Pull `width/height/fps` from the source with `cap.get()` so input and output match.
- Always `out.release()` — this is what actually finishes writing the file.

---

## Additional Explanation — What "fourcc" and "codec" Mean

A **codec** is the algorithm that compresses video (raw video is enormous). **"FOURCC"** = "four character code", a 4-letter tag naming the codec (`mp4v`, `XVID`, `H264`). Different codecs pair with different file extensions.

> If your saved video won't play, a codec/extension mismatch is the usual cause — `mp4v` + `.mp4` is a safe default.

---

# Real-Time Filters (Processing Each Frame)

The pattern is trivial once you have the loop: **whatever you'd do to one image, do it to `frame` inside the loop.**

```python
gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # live grayscale
blur  = cv2.GaussianBlur(frame, (15, 15), 0)          # live blur (Phase 5)
edges = cv2.Canny(frame, 100, 200)                    # live edge detection (Phase 6)
```

That's the whole trick to "real-time filters" — it's Phase 1–3/5–6 operations applied per frame.

> Your YOLO inference (`results = model(frame)`) slots into this exact spot.