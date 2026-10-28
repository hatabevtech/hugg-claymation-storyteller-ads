"""Lay VO + SFX against picture_v2, write captions, mix, mux.

Usage: python3 assemble.py <cut2 dir> <vo dir> <sfx dir>
"""
import json, subprocess, sys

CUT, VO, SFX = sys.argv[1:4]

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", p], capture_output=True, text=True).stdout)

shots = {}
for line in open(f"{CUT}/starts.txt"):
    n, t, d = line.split()
    shots[n] = (float(t), float(d))
total = shots["S24"][0] + shots["S24"][1]

# VO line -> anchor shot (+ offset); captions verbatim from storyboard, "/" = line break, "|" = caption change mid-line
VO_PLAN = [
    ("L01", "S01", 0.0, "Antibiotic ka course / poora kiya."),
    ("L02", "S01", 2.0, "Toh jalan / abhi bhi kyu?"),
    ("L03", "S03", 0.0, "Kyunki H. pylori | saalon tak / aapki lining / khaata raha."),
    ("L04", "S06", 0.0, "Antibiotic ne / bacteria hata diya."),
    ("L05", "S07", 0.0, "Sahi kiya."),
    ("L06", "S08", 0.0, "Par jo lining / usne khaayi, / woh wahi rahi."),
    ("L07", "S09", 0.0, "Isiliye / course ke baad bhi"),
    ("L08", "S10", 0.0, "jalan."),
    ("L09", "S11", 0.0, "Do course. / Teen test. | Phir bhi / wahi pet."),
    ("L10", "S13", 0.0, "Socho: / course khatam, / aur pet bhi shaant."),
    ("L11", "S14", 0.0, "Usi lining pe / TumGard / kaam karta hai."),
    ("L12", "S15", 0.0, "Kalonji / aur licorice / lining ko / support karte hain."),
    ("L13", "S17", 0.0, "Doctor ki dawa / apna kaam kare, / TumGard apna."),
    ("L14", "S18", 0.0, "Chai band nahi. / Bas aadha chammach / lunch ke baad, | aadha dinner ke baad. / 60 din."),
    ("L15", "S20", 0.0, "Log report karte hain: / pehle hafte mein / khane ke baad wali / jalan kam."),
    ("L16", "S21", 0.0, "Aur aap / akele shuru nahi karoge. / Founder ka seedha email, | phir asli nutritionist ka call. / Bot nahi."),
    ("L17", "S23", 0.0, "Course khatam, / aur pet bhi shaant."),
    ("L18", "S24", 0.0, "Buy 2 Get 1, / saath mein free diet plan. / Aaj."),
]

placed, prev_end = [], 0.0
for vid, shot, off, cap in VO_PLAN:
    anchor = shots[shot][0] + off + 0.15
    start = max(anchor, prev_end + 0.25)
    d = dur(f"{VO}/{vid}.wav")
    placed.append((vid, start, d, cap, shot))
    prev_end = start + d

# report overruns: a line still speaking after its shot group has cut away
nxt = {p[0]: (placed[i + 1][1] if i + 1 < len(placed) else total) for i, p in enumerate(placed)}
print("VO placement:")
for vid, s, d, cap, shot in placed:
    late = s - (shots[shot][0] + 0.15)
    print(f"  {vid} {s:6.2f}-{s+d:6.2f}  anchor {shot}{'  LATE +%.2fs' % late if late > 0.05 else ''}")

# SFX: (file, shot, offset, trim_start, length, gain dB)
SFX_PLAN = [
    ("whoosh", "S03", -1.1, 0.0, 2.2, -10),
    ("burp",   "S05", 0.35, 0.0, 0.86, -8),
    ("pop",    "S05", 0.95, 0.0, 0.26, -14),
    ("crack",  "S06", 0.70, 0.0, 0.9, -14),
    ("wave",   "S07", 0.0, 17.8, 2.8, -9),
    ("drip",   "S09", 0.25, 0.0, 0.52, -12),
    ("sizzle", "S09", 0.55, 0.0, 2.0, -14),
    ("chime",  "S15", 0.4, 1.1, 2.4, -2),
    ("drip",   "S16", 0.3, 0.0, 0.52, -12),
    ("ding",   "S21", 0.6, 0.0, 0.37, -12),
]

inputs, filters, labels = [], [], []
for i, (vid, s, d, cap, shot) in enumerate(placed):
    inputs += ["-i", f"{VO}/{vid}.wav"]
    filters.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-16:TP=-2:LRA=7,adelay={int(s*1000)}|{int(s*1000)}[v{i}]")
    labels.append(f"[v{i}]")
base = len(placed)
for j, (f, shot, off, ts, ln, g) in enumerate(SFX_PLAN):
    k = base + j
    t = max(0.0, shots[shot][0] + off)
    inputs += ["-ss", str(ts), "-t", str(ln), "-i", f"{SFX}/{f}.mp3"]
    filters.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={max(0, ln-0.25)}:d=0.25,volume={g}dB,adelay={int(t*1000)}|{int(t*1000)}[s{j}]")
    labels.append(f"[s{j}]")
filters.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:dropout_transition=0,apad,atrim=0:{total},loudnorm=I=-14:TP=-1:LRA=9[mix]")
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filters),
                "-map", "[mix]", "-ar", "48000", "-c:a", "pcm_s16le", f"{CUT}/mix_v2.wav"], check=True)

# captions (ASS): middle third, verbatim, timed to the VO
def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"

ev = []
for i, (vid, s, d, cap, shot) in enumerate(placed):
    end = min(nxt[vid] - 0.05, s + d + 1.2) if i + 1 < len(placed) else total - 0.1
    parts = [p.strip() for p in cap.split("|")]
    weights = [len(p) for p in parts]; span = (s + d) - s
    t0 = s
    for p, w in zip(parts, weights):
        t1 = t0 + span * w / sum(weights)
        e = t1 if p is not parts[-1] else end
        ev.append((t0, e, p.replace(" / ", "\\N"), "CapTop" if vid in ("L11", "L13", "L18") else "Cap"))
        t0 = t1

ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter ExtraBold,66,&H00FFFFFF,&H00FFFFFF,&H00141414,&H96000000,0,0,0,0,100,100,0,0,1,5,3,5,70,70,0,1
Style: CapTop,Inter ExtraBold,66,&H00FFFFFF,&H00FFFFFF,&H00141414,&H96000000,0,0,0,0,100,100,0,0,1,5,3,8,70,70,170,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for a, b, t, st in ev:
    ass += f"Dialogue: 0,{ts(a)},{ts(b)},{st},,0,0,0,,{{\\fad(80,80)}}{t}\n"
open(f"{CUT}/captions_v2.ass", "w").write(ass)
json.dump({"total": total, "vo": [(v, round(s, 2), round(d, 2)) for v, s, d, _, _ in placed]}, open(f"{CUT}/timeline_v2.json", "w"), indent=1)
print("total", round(total, 2))
