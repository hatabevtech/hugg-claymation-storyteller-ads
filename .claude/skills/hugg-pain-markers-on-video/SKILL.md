---
name: hugg-pain-markers-on-video
description: Add hugg's signature red pain marker (a soft red glow on the pain point with sharp lightning bolts flickering out of it) as an animated overlay on a hugg ad video, at the moments where someone physically shows pain (holding the stomach, pressing the chest, doubling over). Use whenever the user uploads a hugg ad cut or video and asks for pain markers, pain overlays, red lightning, "show where it hurts", or similar, even if they don't name this skill. Needs a code environment with ffmpeg and Python (Claude Code), not a plain chat.
---

# hugg pain markers on video

The user uploads one of **our own hugg ad cuts**. You find the moments where the body visibly shows pain, propose them, wait for approval, then render hugg's one signature pain marker at the pain point and hand back:
1. **`preview.mp4`**: the video with markers burned in and the original audio, for review.
2. **`overlay.mov`**: the markers alone on transparency (ProRes 4444 with alpha), same size, length and frame rate. The editor drops it on the track above the video, so markers stay adjustable.

Do all the looking and placing yourself, from the frames. Don't call an external vision model (e.g. Gemini) for this.

## The signature marker (the only marker)

A **soft red glow centred on the pain point**, with **four sharp, filled zigzag bolts** flickering outward from the glow's edge. It pops in with a slight overshoot and fades out at the end. This is the only style. The user tried dots, rings and a glow on its own, and rejected them as useless or inconsistent.

Proportions are fixed fractions of the frame width, so every moment in every video matches. `scripts/render_markers.py` encodes them; don't scale per moment:
- glow radius about 0.15 × width;
- bolts start at the glow's edge and run about 0.22 × width outward.

The one thing you set per moment is the **bolt directions** (`angles`).

## When a moment gets a marker

**Only where the body physically shows pain:** hands clutching or pressing a spot, doubling over, wincing with a hand on the area. Never put a marker:
- where pain is only spoken about ("bloating hoti hai") with neutral body language;
- on hand gestures, explaining, or a person merely touching their clothes;
- in any frame where **the product is visible**, because a pain marker beside the product reads as the product causing pain;
- where it would cover the face, the captions or an existing sticker or graphic.

Expect roughly **1–3 moments in a 30–60 s ad**. Fewer, stronger markers beat many. If nothing qualifies, say so; don't force one.

## Workflow

Copy the upload into a fresh scratch folder first, and run scripts from the skill's `scripts/` folder, not from inside the upload's folder.

### 1. Read the video
```bash
python3 scripts/frames.py info IN.mp4            # size, fps, duration, scene cuts
python3 scripts/frames.py sheet IN.mp4 sheet.jpg  # timestamped contact sheets (sheet_1.jpg, ...)
```
Look at every sheet. Burned-in captions tell you what's being said. Use the scene cuts to snap each moment's start and end to the shot it lives in.

### 2. Propose, then wait
```bash
python3 scripts/frames.py stills IN.mp4 stills.jpg 36.4 38.0   # one still per proposed moment
```
Show the stills and a table: **# · time range (snapped to cuts) · what's happening · pain point · bolt directions**. Mention anything you deliberately skipped and why (spoken-only, product on screen, and so on). **Don't render until the user approves.** They may cut moments or change times.

### 3. Track the pain point
For each approved moment:
```bash
python3 scripts/frames.py grid IN.mp4 START END grid_N.jpg   # 4 fps, 64 px grid in source pixels
```
Read the pain point's position at each frame (between the clutching hands, under the hand on the chest, and so on) and write a `track` of `[t, x, y]` keyframes in **source pixels**. Add a keyframe whenever the body or hand moves; the renderer smooths between them. Then choose `angles` (degrees: 0 = right, −90 = up) so every bolt lands **outside the body's outline**, below the face, above the captions, and clear of stickers. Sideways and diagonal pairs (e.g. `[-150, -30, 195, 345]`) usually work.

Spec file:
```json
{"markers":[
 {"id":1,"start":35.93,"end":36.94,"angles":[-150,-30,195,345],"track":[[35.93,252,388],[36.94,252,388]]}
]}
```

### 4. Render
```bash
python3 scripts/render_markers.py spec.json IN.mp4 OUT_DIR
```

### 5. Check before showing
```bash
python3 scripts/frames.py compare IN.mp4 OUT_DIR/preview.mp4 compare.jpg T1 T2 T3 ...
```
Use at least three times per moment, at full size, source against output. Check:
- the marker sits on the pain point in every frame, including when the body moves;
- the bolts are outside the body, off the face, the captions and stickers;
- the size reads at phone size;
- it appears and disappears inside the shot.

Fix and re-render anything that fails. Also flag problems in the **source** footage that compete with the marker (e.g. a red cast or band from the grade) instead of rendering over them silently.

### 6. Deliver
Send `preview.mp4` (to view) and `overlay.mov` (as an attachment), with a short table of what was marked, what was skipped and why, and any source issues.

## Lessons from the first build
The first pass used 5 moments and 4 marker styles. It looked overused and inconsistent, and the markers were too small. The fixes, now built into this skill:
- one signature style;
- physical pain only;
- fixed, larger proportions;
- bolts placed outside the body;
- full-size checks against the source.
