#!/usr/bin/env python3
"""Frame helpers for placing pain markers. Needs ffmpeg/ffprobe and Pillow.

  python3 frames.py info  IN.mp4                 size, fps, duration, frame count, scene cuts
  python3 frames.py sheet IN.mp4 OUT.jpg [fps]   timestamped contact sheet (default 2 fps)
  python3 frames.py grid  IN.mp4 START END OUT.jpg [fps]
        frames of one moment (default 4 fps) at full source size with a 64 px coordinate
        grid, labelled in source pixels, for reading marker track points
  python3 frames.py stills IN.mp4 OUT.jpg T1 T2 ...   one labelled still per time (proposal sheet)
  python3 frames.py compare SRC.mp4 OUT.mp4 OUT.jpg T1 T2 ...
        full-size source (top) vs rendered (bottom) at each time, for checking
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw

def run(*a): return subprocess.run(a, capture_output=True, text=True, check=True)

def info(path):
    s = json.loads(run("ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                       "stream=width,height,r_frame_rate,nb_frames:format=duration", "-of", "json", path).stdout)
    st = s["streams"][0]; n, d = st["r_frame_rate"].split("/")
    cuts = subprocess.run(["ffmpeg", "-i", path, "-vf", "select='gt(scene,0.2)',showinfo", "-f", "null", "-"],
                          capture_output=True, text=True).stderr
    cuts = [round(float(x.split(":")[1]), 2) for x in cuts.split() if x.startswith("pts_time:")]
    return {"width": st["width"], "height": st["height"], "fps": float(n) / float(d),
            "frames": int(st.get("nb_frames", 0)), "duration": float(s["format"]["duration"]), "cuts": cuts}

def grab(path, t, scale=None):
    fd, tmp = tempfile.mkstemp(suffix=".png"); os.close(fd)
    vf = ["-vf", f"scale={scale}:-2"] if scale else []
    run("ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1", *vf, tmp)
    im = Image.open(tmp).convert("RGB"); os.remove(tmp); return im

def label(im, text):
    d = ImageDraw.Draw(im); d.rectangle([0, 0, 8 * len(text) + 8, 16], fill="black"); d.text((4, 2), text, fill="yellow")
    return im

def tile(ims, cols, out, shrink=1.0):
    w, h = ims[0].size; rows = (len(ims) + cols - 1) // cols
    sh = Image.new("RGB", (cols * w, rows * h), "white")
    for i, im in enumerate(ims): sh.paste(im, ((i % cols) * w, (i // cols) * h))
    if shrink != 1.0: sh = sh.resize((int(sh.width * shrink), int(sh.height * shrink)))
    sh.save(out, quality=88)

def main():
    cmd, path = sys.argv[1], sys.argv[2]
    if cmd == "info":
        print(json.dumps(info(path), indent=1)); return
    meta = info(path)
    if cmd == "sheet":
        out = sys.argv[3]; fps = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
        ts = [i / fps for i in range(int(meta["duration"] * fps))]
        ims = [label(grab(path, t, 240), f"{t:.1f}s") for t in ts]
        for k in range(0, len(ims), 50):
            tile(ims[k:k + 50], 10, out.replace(".jpg", f"_{k // 50 + 1}.jpg"))
    elif cmd == "grid":
        a, b, out = float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
        fps = float(sys.argv[6]) if len(sys.argv) > 6 else 4.0
        ims = []; t = a
        while t <= b + 1e-6:
            im = grab(path, t); d = ImageDraw.Draw(im); W, H = im.size
            for x in range(0, W, 64): d.line([(x, 0), (x, H)], fill=(0, 255, 255)); d.text((x + 2, 2), str(x), fill=(0, 255, 255))
            for y in range(0, H, 64): d.line([(0, y), (W, y)], fill=(0, 255, 255)); d.text((2, y + 2), str(y), fill=(0, 255, 255))
            ims.append(label(im, f"{t:.2f}s")); t += 1 / fps
        tile(ims, min(4, len(ims)), out, 0.75)
    elif cmd == "stills":
        out, ts = sys.argv[3], [float(x) for x in sys.argv[4:]]
        tile([label(grab(path, t, 320), f"{i + 1} · {t:.1f}s") for i, t in enumerate(ts)], 3, out)
    elif cmd == "compare":
        rendered, out, ts = sys.argv[3], sys.argv[4], [float(x) for x in sys.argv[5:]]
        top = [label(grab(path, t), f"src {t:.2f}s") for t in ts]
        bot = [label(grab(rendered, t), f"out {t:.2f}s") for t in ts]
        tile(top + bot, len(ts), out, 0.5 if len(ts) > 3 else 0.75)

if __name__ == "__main__":
    main()
