#!/usr/bin/env python3
"""Render the hugg pain marker (red glow + sharp bolts) onto a video.

Usage: python3 render_markers.py SPEC.json IN.mp4 OUT_DIR
SPEC = {"markers":[{"id":5,"start":35.95,"end":36.95,"angles":[-145,-35,190,350],
         "track":[[t,x,y],...]}]}   # angles: bolt directions in degrees (0 = right, -90 = up)   # x,y in source pixels; track is interpolated
Writes OUT_DIR/overlay.mov (ProRes 4444 with alpha, for the edit) and
OUT_DIR/preview.mp4 (markers burned in, original audio).
"""
import json, math, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFilter

RED = (225, 30, 35)

def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,r_frame_rate,nb_frames", "-of", "json", path],
                         capture_output=True, text=True, check=True).stdout
    s = json.loads(out)["streams"][0]
    n, d = s["r_frame_rate"].split("/")
    return s["width"], s["height"], float(n) / float(d), int(s["nb_frames"])

def pos(track, t):
    if t <= track[0][0]: return track[0][1:]
    for a, b in zip(track, track[1:]):
        if a[0] <= t <= b[0]:
            k = (t - a[0]) / (b[0] - a[0]) if b[0] > a[0] else 0
            k = k * k * (3 - 2 * k)  # smoothstep between keyframes
            return [a[1] + (b[1] - a[1]) * k, a[2] + (b[2] - a[2]) * k]
    return track[-1][1:]

def envelope(t, start, end):
    """Pop-in with overshoot, hold, fade-out. Returns (scale, alpha)."""
    a = t - start; b = end - t
    if a < 0 or b < 0: return 0, 0
    pop = 0.2
    if a < pop:
        x = a / pop
        sc = 1 + 0.18 * math.sin(math.pi * x) if x > 0.5 else x * 2 * 1.0
        sc = max(sc, 0.05)
    else:
        sc = 1
    al = min(1, a / 0.12, b / 0.2)
    return sc, al

def glow(layer, x, y, r, t, al):
    g = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    p = 0.5 + 0.5 * math.sin(t * 2 * math.pi * 2.2)
    for i, (f, a) in enumerate([(1.0, 70), (0.7, 90), (0.42, 110)]):
        rr = r * f * (0.9 + 0.15 * p)
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=RED + (int(a * (0.65 + 0.35 * p) * al),))
    g = g.filter(ImageFilter.GaussianBlur(r * 0.35))
    layer.alpha_composite(g)

# Classic lightning-bolt icon, pointing along +x, length 1.0 (filled polygon).
BOLT = [(0.0, -0.10), (0.55, -0.16), (0.42, -0.02), (1.0, -0.10), (0.30, 0.20), (0.44, 0.04), (0.0, 0.12)]

def bolt_poly(x, y, ang, r0, length, flip):
    c, s_ = math.cos(ang), math.sin(ang); pts = []
    for (u, v) in BOLT:
        v = -v if flip else v
        px, py = r0 + u * length, v * length
        pts.append((x + px * c - py * s_, y + px * s_ + py * c))
    return pts

def lightning(layer, x, y, r, t, al, fps, angles):
    d = ImageDraw.Draw(layer)
    fr = int(t * fps)
    if (fr // 3) % 5 == 4: return  # quick flicker off
    jit = 1 + 0.08 * math.sin(fr * 1.3)
    for k, base in enumerate(angles):
        ang = math.radians(base + 5 * math.sin(fr * 0.6 + k))
        pts = bolt_poly(x, y, ang, r * 1.0, r * 1.55 * jit, flip=(k % 2 == 1))
        d.polygon(pts, fill=(0, 0, 0, int(70 * al)), outline=(0, 0, 0, int(110 * al)), width=3)
        d.polygon(pts, fill=RED + (int(250 * al),))

def main():
    spec, src, out = sys.argv[1:4]
    os.makedirs(out, exist_ok=True)
    W, H, fps, n = probe(src)
    markers = json.load(open(spec))["markers"]
    # One signature marker, fixed proportions of the frame width so every moment matches:
    # a soft red glow on the pain point, with sharp bolts flickering out from its edge.
    GLOW_R = 0.15 * W        # glow radius
    BOLT_R = 0.142 * W       # bolts start at ~the glow edge and run ~0.22 W outward
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}",
                            "-r", str(fps), "-i", "-", "-c:v", "prores_ks", "-profile:v", "4444",
                            "-pix_fmt", "yuva444p10le", os.path.join(out, "overlay.mov")], stdin=subprocess.PIPE)
    empty = bytes(W * H * 4)
    for f in range(n):
        t = f / fps
        live = [m for m in markers if m["start"] <= t <= m["end"]]
        if not live:
            enc.stdin.write(empty); continue
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for m in live:
            sc, al = envelope(t, m["start"], m["end"])
            x, y = pos(m["track"], t)
            glow(layer, x, y, GLOW_R * sc, t, al)
            lightning(layer, x, y, BOLT_R * sc, t, al, fps, m.get("angles", [-145, -35, 190, 350]))
        enc.stdin.write(layer.tobytes())
    enc.stdin.close(); enc.wait()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-i", os.path.join(out, "overlay.mov"),
                    "-filter_complex", "[0:v][1:v]overlay=0:0:format=auto[v]", "-map", "[v]", "-map", "0:a?",
                    "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "copy",
                    os.path.join(out, "preview.mp4")], check=True)
    print("done", W, H, fps, n)

if __name__ == "__main__":
    main()
